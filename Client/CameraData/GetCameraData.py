import serial
import binascii
import time

ser = serial.Serial()


#command for Cam1:  0 is get number of customers in and out 
#                   1 is reset counter
#                   2 is check door status
command_Cam1 =  [   [0x02,0x30,0x30,0x30,0x31,0x31,0x33,0x30,0x30,0x31,0x34,0x03],
                    [0x02,0x30,0x30,0x30,0x31,0x31,0x32,0x30,0x30,0x31,0x33,0x03],
                    [0x02,0x30,0x30,0x30,0x31,0x36,0x36,0x30,0x36,0x36,0x44,0x03]
                ]

# ID: 0002 (example)
command_Cam2 = [    [0x02,0x30,0x30,0x30,0x32,0x31,0x33,0x30,0x30,0x31,0x35,0x03],
                    [0x02,0x30,0x30,0x30,0x32,0x31,0x32,0x30,0x30,0x31,0x34,0x03],
                    [0x02,0x30,0x30,0x30,0x32,0x36,0x36,0x30,0x36,0x36,0x45,0x03]
                ]

# open serial port
def initSerial():
    global ser
    ser.baudrate = 9600
    ser.port = 'COM13'
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
    ser.timeout = 0.3
    
# send data to processor of Camera 1
def sendData(number):  
    ser.write(serial.to_bytes(command_Cam1[number]))
    
def sendDataToCam2(number):
    ser.write(serial.to_bytes(command_Cam2[number]))
    
# get data from processor
def getDataPackage():
    res = ""
    while True:
        mHex = ser.read()
        if len(mHex) == 0:
            res = "No Data"
            break
        if len(mHex) != 0 and mHex.decode('utf-8') == "\x02": 
            continue
        if len(mHex) != 0 and mHex.decode('utf-8') == "\x03": 
            break
        if len(mHex)!= 0:
            res = res + mHex.decode('utf-8')
        time.sleep(0.001) 
    return res

# get id
def getIDFromPackage(data):
    id = ""
    for i in range(0,4) : 
        id = id + data[i]
    return id

# get command character
def getCommandCharacterFromPackage(data):
    cm = ""
    # CM
    for i in range(4,6):
        cm = cm + data[i]
    return cm

# get passenger flow
def getPassengerFlow( data ):
    # example data
    # 0001/93/10/00000007/00000002/00000000/00000000/AD/
    dataLen1 = data[6]
    dataLen2 = data[7]
    numIn = ""
    numOut = ""

    for i in range(8, 16):
        numIn = numIn + data[i]
    for i in range(16, 24):
        numOut = numOut + data[i]
    numIn = int(numIn, base = 16)
    numOut = int(numOut , base = 16)
    
    return (numIn, numOut)

# Get DoorStatus of Camera1
def getDoorStatusCam1():
    # example data
    # 0001/E6/06/01/0101010101/F3
    sendData(2)
    data = getDataPackage()
    doorStatus = ""
    doorStatus = doorStatus + data[10] + data[11]
    doorStatus = 1 - int(doorStatus, base = 16)
    return doorStatus

# Get DoorStatus of Camera2
def getDoorStatusCam2():
    # example data
    # 0001/E6/06/01/0101010101/F3
    sendDataToCam2(2)
    data = getDataPackage()
    doorStatus = ""
    doorStatus = doorStatus + data[10] + data[11]
    doorStatus = 1 - int(doorStatus, base = 16)
    return doorStatus

# Data Structure:
    # if no data:   data = CamData:idCam/'NoData' (CamData:0001/Nodata)
    # else :        data = CamData:idCam/numIn / numOut / doorStatus/ camStatus (0001/3/3/0/1)
def getDataStream():
    # Cam1
    dataStream = "CamData:0001/"
    # send command to camera to get data
    sendData(0)
    dataPackage = getDataPackage()
    
    if dataPackage == "No Data":
        dataStream += "NoData"
    else :
        idCam = getIDFromPackage(dataPackage)
        passFlow = getPassengerFlow(dataPackage)
        numIn = passFlow[0] 
        numOut = passFlow[1]
        doorStatus = getDoorStatusCam1()
        dataStream = 'CamData:'+ idCam + '/' +  str(numIn) + '/' + str(numOut) + '/' + str(doorStatus) + '/1' 
    
    return dataStream
    
def getDataStream2():
    # Cam1
    dataStream = "CamData:0002/"
    # send command to camera to get data
    sendDataToCam2(0)
    dataPackage = getDataPackage()
    
    if dataPackage == "No Data":
        dataStream += "NoData"
    else :
        idCam = getIDFromPackage(dataPackage)
        passFlow = getPassengerFlow(dataPackage)
        numIn = passFlow[0] 
        numOut = passFlow[1]
        doorStatus = getDoorStatusCam2()
        
        dataStream ='CamData:' + idCam + '/' +  str(numIn) + '/' + str(numOut) + '/' + str(doorStatus) + '/1' 
    
    return dataStream

# Reset Counter
def resetCounter():
    # Reset Counter from Camera 1
    sendData(1)
    data = getDataPackage()
    
    time.sleep(0.01)
    
     # Reset Counter from Camera 2
    sendDataToCam2(1)
    data = getDataPackage()
    


# def main():
#     global ser
#     initSerial()
#     ser.open()
    
#     time.sleep(0.1)
    
#     last = round(time.time())
#     while True:
#         cur = round(time.time())
#         if(cur- last >= 3):
#             time.sleep(0.01)
            
#             data1 = getDataStream()
            
#             data2 = getDataStream2()

            
#             print(data1 , data2)
#             last = cur

# if __name__ == "__main__":
#     main()