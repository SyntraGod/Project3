from tkinter import *
from tkinter import messagebox
from tkinter import font

from datetime import datetime
from threading import Thread

from GetCameraData import *
from GetGPS import *
from RandomCameraData import *
from FileHandler import *
from SendDataToServer import *

DVQL = "Bus Hà Nội"
Tuyen = "32"
BKS = "30B-23214"
lastDoorStatus = currentDoorStatus = 'Close'
simId = ""


global rootWindow

# main Window
rootWindow = Tk()
rootWindow.title("Thông tin xe bus")
rootWindow.state("zoom")

# Title Label
title_Label = Label(rootWindow, text = "THÔNG TIN XE BUS",
                    font = font.Font(size = 30, weight='bold'), fg = "red",
                    pady = 10)
title_Label.pack()

# Date and time label
date_Label = Label(rootWindow, font = font.Font(size = 15, weight="bold"),
                   width = 110, height= 2,
                   borderwidth = 1, relief= "solid",
                   bg = "lightgray", )
date_Label.pack()

# DVQL Label
DVQL_Label = Label(rootWindow, text= "Đơn vị quản lý : " + DVQL, 
                   font = font.Font(size = 15, weight="bold"), 
                   width = 110, height= 2,
                   borderwidth = 1, relief= "solid",
                   bg = "lightgray", 
                   )
DVQL_Label.pack()

# Tuyen Label
Tuyen_Label = Label(rootWindow, text= "Tuyến : " + Tuyen, 
                   font = font.Font(size = 15, weight="bold"), 
                   width = 110, height= 2,
                   borderwidth = 1, relief= "solid",
                   bg = "lightgray",
                   )
Tuyen_Label.pack()

# BKS Label
BKS_Label = Label(rootWindow, text= "Biển kiểm soát : " + BKS, 
                   font = font.Font(size = 15, weight="bold"), 
                   width = 110, height= 2,
                   borderwidth = 1, relief= "solid",
                   bg = "lightgray",
                   )
BKS_Label.pack()
   
# Passenger In-Out Label
IO_Frame = Frame(rootWindow)
IO_Frame.pack()
in_Label = Label( IO_Frame,  text="Số khách vào",
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 2,
                  borderwidth = 1, relief= "solid",
                  bg = "green",
                  )
in_Label.grid(row=0, column=0)

# Out Label
out_Label = Label( IO_Frame,  text="Số khách ra",
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 2,
                  borderwidth = 1, relief= "solid",
                  bg = "red",
                  )
out_Label.grid(row=0, column=1)

# Passenger In-Out Value
IOVal_Frame = Frame(rootWindow)
IOVal_Frame.pack()
inVal_Label = Label( IOVal_Frame,
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 4,
                  borderwidth = 1, relief= "solid",
                  bg = "white",
                  )
inVal_Label.grid(row=0, column=0)

# Out Label
outVal_Label = Label( IOVal_Frame,
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 4,
                  borderwidth = 1, relief= "solid",
                  bg = "white",
                  )
outVal_Label.grid(row=0, column=1)

# Current Passenger Label
cur_Label = Label(rootWindow, text= "Số khách trên xe", 
                   font = font.Font(size = 15, weight="bold"), 
                   width = 110, height= 2,
                   borderwidth = 1, relief= "solid",
                   bg = "yellow",
                   )
cur_Label.pack()

# Display number of passenger
curVal_Label =  Label(rootWindow, 
                   font = font.Font(size = 15, weight="bold"), 
                   width = 110, height= 4,
                   borderwidth = 1, relief= "solid",
                   bg = "white",
                   )
curVal_Label.pack()

# Camera
Cam_Frame = Frame(rootWindow)
Cam_Frame.pack()
# Cam 1
cam_Label1 = Label( Cam_Frame,
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 2,
                  borderwidth = 1, relief= "solid",
                  bg = "lightgray",
                  )
cam_Label1.grid(row=0, column=0)

# Cam 2
cam_Label2 = Label( Cam_Frame,
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 2,
                  borderwidth = 1, relief= "solid",
                  bg = "lightgray",
                  )
cam_Label2.grid(row=0, column=1)

# Door
Door_Frame = Frame(rootWindow)
Door_Frame.pack()
# Door1
door_Label1 = Label( Door_Frame,
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 2,
                  borderwidth = 1, relief= "solid",
                  bg = "lightgray",
                  )
door_Label1.grid(row=0, column=0)

# Door 2
door_Label2 = Label( Door_Frame,
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 2,
                  borderwidth = 1, relief= "solid",
                  bg = "lightgray",
                  )
door_Label2.grid(row=0, column=1)

# Position
Pos_Frame = Frame(rootWindow)
Pos_Frame.pack()
# Latitude
lat_Label = Label( Pos_Frame,
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 2,
                  borderwidth = 1, relief= "solid",
                  bg = "lightgray",
                  )
lat_Label.grid(row=0, column=0)

# Longtitude
lon_Label = Label( Pos_Frame,
                  font = font.Font(size = 15, weight="bold"), 
                  width = 55, height= 2,
                  borderwidth = 1, relief= "solid",
                  bg = "lightgray",
                  )
lon_Label.grid(row=0, column=1)



''' 
                                    UPDATE DATA TO WINDOW
'''
totalNumIn = 0
totalNumOut = 0
cur = 0

def autoUpdateData():
    global totalNumOut, totalNumIn, cur, simId
    global lastDoorStatus, currentDoorStatus
    
    # Get Camera Data From Camera 1:
    # Data to test
    # CamData1 = randomCamData1()
    
    CamData1 = getDataStream()
    CameraData1 = CamData1.split(':')[1]
    if(CameraData1 == '0001/NoData'):
        idCam1 = '0001'
        numIn1 = 0
        numOut1 = 0
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
        numIn2 = 0
        numOut2 = 0
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
        currentTime = datetime.now()
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
    
    # Current DoorStatus
    if doorStatus1 == 'Open' or doorStatus2 == 'Open':
        currentDoorStatus = 'Open'
    else: 
        currentDoorStatus = 'Close'
    
    # Bus has just left Station: send all data
    if currentDoorStatus == 'Close' and lastDoorStatus == 'Open':  
        totalNumIn += (numIn1 + numIn2)
        totalNumOut += (numOut1 + numOut2)
        cur = totalNumIn - totalNumOut
        
        dataToSend = {
                "_id" : simId,
                "lat" : lat,
                "lon": long,
                "alt": alt,
                "tim" : dateAndTime,
                "spd": spd,
                "nav": nav,
                "cur" : cur,
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
            "_id" : simId,
            "lat" : lat,
            "lon": long,
            "alt": alt,
            "tim" : dateAndTime,
            "spd": spd,
            "nav": nav,
            "cur" : cur, 
        }
    
    lastDoorStatus = currentDoorStatus
    
    SendDataToServer(dataToSend)
    
   #  Display In/Out Data
    inVal_Label["text"] = totalNumIn
    outVal_Label["text"] = totalNumOut
    curVal_Label["text"] = cur
    
   #  Display camera Status
    cam_Label1["text"] = "Camera 1: " + camStatus1
    cam_Label2["text"] = "Camera 2: " + camStatus2
    
    #  Display door Status
    if doorStatus1 == None : doorStatus1 = "Mất tín hiệu"
    if doorStatus2 == None : doorStatus2 = "Mất tín hiệu"
    door_Label1["text"] = "Cửa trước: " + doorStatus1
    door_Label2["text"] = "Cửa sau: " + doorStatus2
        
   #  Display Position 
    lat_Label["text"] = "Vĩ độ: " + str(lat)
    lon_Label["text"] = "Kinh độ: " + str(long)
        
    rootWindow.after(2000, autoUpdateData) # run itself again after 3000 ms

def autoUpdateTime():
   # Auto update time
   currentTime = datetime.now()
   dateAndTime = currentTime.strftime("%d/%m/%Y - %H:%M:%S")
   date_Label['text'] = "Ngày - giờ : " + dateAndTime
   
   rootWindow.after(1000, autoUpdateTime) # run itself again after 1000 ms

def runWindow():
    global simId
    simId = GetSimID()
    
   # Auto update time
    Thread1 = Thread( target = autoUpdateTime )
    Thread2 = Thread( target = autoUpdateData )
   
    Thread1.start() 
    Thread2.start()


def main():
    # Open Serial for Camera data
    try:
        global ser
        initSerial()
        ser.open()
        WriteToFile('Open Camera PORT successfully!')
    except:
        # Show message box if error
        WriteToFile('Can not open Camera PORT!') 
        Error = messagebox.showerror(title='LỖI', message="Không thể mở cổng PORT Camera! \n Vui lòng kiểm tra lại dây cắm!")
        raise
    
    # Open Serial for GPS Data
    try:
        global GPS_ser
        initGPSSerial()
        GPS_ser.open() 
        # Init GPS
        initGPS()
        WriteToFile('Open GPS PORT successfully!')  
    except:
        WriteToFile('Can not open GPS PORT!') 
        Error = messagebox.showerror(title='LỖI', message="Không thể mở cổng PORT GPS! \n Vui lòng kiểm tra lại dây cắm!")
        raise
    
    runWindow()
    rootWindow.mainloop()
    

if __name__ == '__main__':
    main()
    