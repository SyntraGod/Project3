import serial
import binascii
import time
from datetime import date, datetime
from DBConnection import *

ser = serial.Serial()
conn = DBConnect("localhost", "root", "20102001", "project3")

#command:   0 is get number of customers in and out 
#           1 is reset counter
#           2 is check door status
command =   [   [0x02,0x30,0x30,0x30,0x31,0x31,0x33,0x30,0x30,0x31,0x34,0x03],
                [0x02,0x30,0x30,0x30,0x31,0x31,0x32,0x30,0x30,0x31,0x33,0x03],
                [0x02,0x30,0x30,0x30,0x31,0x36,0x36,0x30,0x36,0x36,0x44,0x03]
            ]

# open serial port
def initSerial():
    global ser
    ser.baudrate = 9600
    ser.port = 'COM3'
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
    
# send data to processor
def sendData(number):  
    ser.write(serial.to_bytes(command[number]))
    
# get data from processor
def getDataPackage():
    res = ""
    while True:
        mHex = ser.read()
        if len(mHex) != 0 and mHex.decode('utf-8') == "\x02": 
            continue
        if len(mHex) != 0 and mHex.decode('utf-8') == "\x03": 
            break
        if len(mHex)!= 0:
            res = res + mHex.decode('utf-8')
        time.sleep(0.01) 
        
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

def getDoorStatus():
    # example data
    # 0001/E6/06/01/0101010101/F3
    sendData(2)
    data = getDataPackage()
    doorStatus = ""
    doorStatus = doorStatus + data[10] + data[11]
    doorStatus = 1 - int(doorStatus, base = 16)
    return doorStatus

# update passenger flow to db
def updateDataToDB():
    # send request to get passenger flow
    sendData(0)
    
    # get data 
    dataPackage = getDataPackage()
    
    idBus = getIDFromPackage(dataPackage)
    passFlow = getPassengerFlow(dataPackage)
    numIn = passFlow[0] 
    numOut = passFlow[1]
    dateBus = date.today()
    statusBus = getDoorStatus()
    
    data1 = getDataByID(conn, idBus)

    # if id is not available, insert into database
    if len(data1) == 0:
        InsertData(conn, idBus, numIn , numOut , dateBus , statusBus)
    else:  UpdateData(conn, idBus, numIn , numOut , dateBus , statusBus)
    
# Reset Counter
def resetCounter():
    sendData(1)
    data = getDataPackage()
    

def Loop():
    initSerial()
    global ser, conn
    ser.open()  
    
    lastTime = round(time.time())
    while 1:
        cur = round(time.time())
        if(cur - lastTime >= 1):
            lastTime = cur
            updateDataToDB()
    
    ser.close()
    
