# import socket, ssl
import time
import json
import requests

from CameraData.GetCameraData import *
from GPSModule.GetGPS import *

from datetime import datetime


from RandomForTesting.RandomCameraData import *

# Socket
# clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 9999  # The port used by the server

url = 'https://service.vst.edu.vn/api/bus'

lastDoorStatus = 'Close'
currentDoorStatus = ''

# The Structure of Data
'''
if the bus leaves the station, send data:
    {
        "_id" : SimID,
        "lat" : lat,
        "lon": long,
        "alt": alt,
        "tim" : dateAndTime <YYYY-MM-DDTHH:MM:SS,
        "spd": spd,
        "nav": nav,
        "cams" :[{
            "i": numIn1,
            "o" : numOut1,
            "d": doorStatus1,
            "c" : camStatus1 
        },
        {
            "i": numIn2,
            "o" : numOut2,
            "d": doorStatus2,
            "c" : camStatus2 
        }
        ]   
    }
    
    if the bus is moving, send data:
    {
        "_id" : SimID,
        "lat" : lat,
        "lon": long,
        "alt": alt,
        "tim" : dateAndTime <YYYY-MM-DDTHH:MM:SS,
        "spd": spd,
        "nav": nav,
        cams : None 
    }
'''
# GPS:
'''
    if 'No data':   GPSData = GPS:NoData
    else:           GPSData = GPS:lat/long/alt/dateAndTime/spd/nav
'''
# Camera:
'''
    if no data:     CameraData = CamData:idCam/'NoData' (CamData:0001/Nodata)
    # else :        CameraData = CamData:idCam/numIn / numOut / doorStatus/ camStatus (CamData:0001/3/3/0/1)
'''
# SIMID:
'''
    20 digits
'''
# Date and Time: YYYY-MM-DDTHH:MM:SS
def DataToSend():
    global lastDoorStatus
    
    # Get Camera Data From Camera 1:
    # Data to test
    # CamData1 = randomCamData1()
    
    CamData1 = getDataStream()
    CameraData1 = CamData1.split(':')[1]
    if(CameraData1 == '0001/NoData'):
        idCam1 = '0001'
        numIn1 = None
        numOut1 = None
        doorStatus1 = None
        camStatus1 = 'Off'
    else:
        idCam1, numIn1, numOut1, doorStatus1, camStatus1 = CameraData1.split('/')
        numIn1 = int(numIn1)
        numOut1 = int(numOut1)
        if doorStatus1 == '1': 
            doorStatus1 = 'Close'
        else:
            doorStatus1 = 'Open'
        if camStatus1 == '1':
            camStatus1 = 'On'
        else:
            camStatus1 = 'Off'
            
    # time.sleep(0.1)
    
    # Get Camera Data From Camera 2:
    # Data to test
    # CamData2 = randomCamData2()
    
    CamData2 = getDataStream2()
    CameraData2 = CamData2.split(':')[1]
    if(CameraData2 == '0002/NoData'):
        idCam2 = '0002'
        numIn2 = None
        numOut2 = None
        doorStatus2 = None
        camStatus2 = 'Off'
    else:
        idCam2, numIn2, numOut2, doorStatus2, camStatus2 = CameraData2.split('/')
        numIn2 = int(numIn2)
        numOut2 = int(numOut2)
        if doorStatus2 == '1': 
            doorStatus2 = 'Close'
        else:
            doorStatus2 = 'Open'
        if camStatus2 == '1':
            camStatus2 = 'On'
        else:
            camStatus2 = 'Off'
    
    # time.sleep(0.1)
    
    # Get GPS Data
    # Data to test
    # GPSDataPackage = 'GPS:1/1/6.6/2024-05-04T12:34:27/0.0/0.0'
    
    GPSDataPackage = getGPSInfo()
    GPSData = GPSDataPackage.split(':',1)[1]
    
    if GPSData == 'NoData':
        lat = None
        long = None
        alt = None
        currentTime = datetime.datetime.now()
        dateAndTime = currentTime.strftime("%Y-%m-%dT%H:%M:%S")
        spd = None
        nav = None
    else:
        lat, long, alt, dateAndTime, spd, nav = GPSData.split('/')
        lat = float(lat)
        long = float(long)
        alt = float(alt)
        spd = float(spd)
        
    # time.sleep(0.1)
    
    # Get SIMID
    # # Data to test
    # SimID = '89840480000633526662'
    SimID = GetSimID()
    
    # Current DoorStatus
    if doorStatus1 == 'Open' or doorStatus2 == 'Open':
        currentDoorStatus = 'Open'
    else: 
        currentDoorStatus = 'Close'
    
    # Bus has just left Station: send all data
    if currentDoorStatus == 'Close' and lastDoorStatus == 'Open':  
        dataToSend = {
                "_id" : SimID,
                "lat" : lat,
                "lon": long,
                "alt": alt,
                "tim" : dateAndTime,
                "spd": spd,
                "nav": nav,
                "cams" :[{
                    "i": numIn1,
                    "o" : numOut1,
                    "d": doorStatus1,
                    "c" : camStatus1 
                },
                {
                    "i": numIn2,
                    "o" : numOut2,
                    "d": doorStatus2,
                    "c" : camStatus2 
                }
                ]   
            }
        
        # # Reset counter
        resetCounter()
    else :
        dataToSend = {
            "_id" : SimID,
            "lat" : lat,
            "lon": long,
            "alt": alt,
            "tim" : dateAndTime,
            "spd": spd,
            "nav": nav,
            "cams" : None   
        }
    
    lastDoorStatus = currentDoorStatus
    
    print(CamData1 + '\n' + CamData2 )
    
    return dataToSend

def main():
    # # Connect to server 
    # clientSocket.connect((HOST, PORT))
    
    # Open Serial for Camera data
    global ser
    initSerial()
    ser.open()  
    
    # Open Serial for GPS Data
    global GPS_ser
    initGPSSerial()
    GPS_ser.open() 
    
    # Init GPS
    initGPS()
    
    lastTime = round(time.time())
    
    while True:
        # Send data to server every 3 seconds
        cur = round(time.time())
        
        
        if(cur - lastTime >= 3):
            dataToSend = DataToSend()
            print(dataToSend)
            
            json_dataToSend = json.dumps(dataToSend)
            
            # Make Post request
            response = requests.post(url, json=json_dataToSend)
            
            # Check the response
            if response.status_code == 200:
                print(response.text)
            else:
                print("Error:", response.status_code)
                print(response.text)
            
            lastTime = cur

    # ser.close()
    # GPS_ser.close()

if __name__ == '__main__':
    main()
    
    