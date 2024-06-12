import random
import serial
import time
import datetime

from FileHandler import *
from tkinter import messagebox
from datetime import datetime

GPS_ser = serial.Serial()


#   command 0: Test connection
#   command 1: Open GPS
#   command 2: Get GPS Info
#   command 3: Close GPS
#   command 4: Check if SIM card is ready
#   command 5: Get SIM ID
command = ['AT',
           'AT+CGPS=1',
           'AT+CGPSINFO',
           'AT+CGPS=0',
           'AT+CPIN?',
           'AT+CCID']

def initGPSSerial():
    global GPS_ser
    GPS_ser.baudrate = 9600
    GPS_ser.port = 'COM12'
    GPS_ser.stopbits = serial.STOPBITS_ONE
    GPS_ser.bytesize = 8
    GPS_ser.parity = serial.PARITY_NONE
    GPS_ser.rtscts = 0
    GPS_ser.timeout = 0.3

def sendData(index):
    try:
        text_data = command[index] + '\r\n'
        GPS_ser.write(text_data.encode())
    except:
        Error = messagebox.showerror(title='LỖI', message= 'Không thể gửi bản tin tới thiết bị GPS! \n Vui lòng kiểm tra lại!')
        WriteToFile('Can not send data to GPS Module!')
        raise

# Initialize GPS module
def initGPS():
        res = ''
        # send AT command to test connection
        sendData(0)
        time.sleep(0.01)
        res = getData()
        
        time.sleep(0.01)
        
        # Open GPS Mode
        sendData(1)
        time.sleep(0.01)
        res = getData()
    
def closeGPS():
    # Close GPS Mode
    sendData(3)
    time.sleep(0.01)
    res = getData()
    
# GPSINFO data: latitude, longtitude, date, time, altitude, speed and navigation angle
# +CGPSINFO: 2100.327114,N,10550.693436,E,250424,024307.0,32.5,0.0,
def getData():
    try:
        res = GPS_ser.read_all()
        return res.decode('utf-8') 
    except:
        WriteToFile('Can not receive data from GPS Module!')
        return None

# Get data package
def ProcessData(data):
    if data == None or data == '':
        WriteToFile('GPS Package loss')
        data = 'GPSInfo:Nodata'
    label, dataPackage = data.split(':')
    dataPackage.lstrip()
    return label, dataPackage

# get SIM number
def GetSimID():
    try:
        # # check SIM Status
        # sendData(4)
        # time.sleep(0.01)
        # dataPackage = getData()
        
        # Get Sim Number
        sendData(5)
        time.sleep(0.01)
        dataPackage = getData()
        
        label, simID = dataPackage.split(':')
        simID = simID[1:21]
        return simID
    except:
        WriteToFile('Can not get SIMID!')
        Error = messagebox.showerror(title='LỖI', message= 'Không thể lấy được thông tin SimID! \n Vui lòng kiểm tra lại thiết bị 4G!')
        raise

# get GPS data
def GetGPSData(dataPackage):
    lat, dir1, long, dir2, date, time, alt, spd, nav = dataPackage.split(',')
    try:
        lat = float ( int(float(lat) / 100) + float (float(lat) % 100) / 60 )
    except:
        lat = 'NoData'
    try:
        long = float ( int (float(long) / 100) + float (float(long) % 100) / 60 )
    except:
        long = 'NoData'
    try:
        alt = float(alt)
    except:
        alt = 'NoData'
    try:
        spd = float(spd)
    except:
        spd = 'NoData'
    return lat, dir1, long, dir2, date, time, alt, spd, nav     

# GPSData = GPS:lat/long/alt/dateAndTime/spd/nav
def getGPSInfo():
    GPSData = 'GPS:'
    # get GPS data
    sendData(2)
    
    time.sleep(0.1)
    
    data = getData()
    
    if data == None:
        GPSData+='NoData'
    else:
        label , dataPackage = ProcessData(data)
    
        dataPackage = dataPackage.split('\n')[0]
        
        if len(dataPackage) <= 10:
            GPSData += 'NoData'
        else:
            lat, dir1, long, dir2, date, Time, alt, spd, nav = GetGPSData(dataPackage)
            
            # Get date and time
            currentTime = datetime.now()
            dateAndTime = currentTime.strftime("%Y-%m-%dT%H:%M:%S")
            
            GPSData += str(lat)  + '/' + str(long)  + '/' + str(alt) + '/'  + dateAndTime + '/' + str(spd) +'/' + nav
    return GPSData

# def main():
#     global GPS_ser
#     initGPSSerial()
#     GPS_ser.open() 
    
#     time.sleep(0.1)
    
#     # Init GPS
#     initGPS()
    
#     time.sleep(0.1)
    
#     last = round(time.time())
#     while True:
#         cur = round(time.time())
#         if(cur- last >= 3):
            
#             print("?")
#             sendData(2)
#             time.sleep(0.01)
#             data = getData()
#             print(data + '\n')
            
#             simid = GetSimID()
            
#             print(simid)
#             last = cur
    
# if __name__ == '__main__':
#     main()
