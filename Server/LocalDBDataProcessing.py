from DBConnection import *
import time

conn = DBConnect("localhost", "root", "20102001", "project3")

def initDB():
    data1 = getDataByID(conn, '0001')
    # if id is not available, insert into database
    if len(data1) == 0:
        InsertData(conn, '0001', 0 , 0  , 1)
        
    data1 = getDataByID(conn, '0002')
    # if id is not available, insert into database
    if len(data1) == 0:
        InsertData(conn, '0002', 0 , 0  , 1)
        

# Data Structure:
    # if no data:   data = idCam : 'No Data' (0001/No data)
    # else :        data = idCam :  numIn / numOut / doorStatus/ camStatus
# update passenger flow to db
def updateDataToDB(dataPackage):
    # Split data
    dataStream = dataPackage.split(':')
    idCam = dataStream[0]
    package = dataStream[1]
    
    # Check current camStatus: 0 is off, 1 is on
    if package == "NoData":
        UpdateCamStatus(conn, idCam , 0)
    else :
        UpdateCamStatus(conn, idCam, 1)
        data = package.split('/')
        numIn = data[0]
        numOut = data[1]
        doorStatus = data[2]
        
        data1 = getDataByID(conn, idCam)

        # if id is not available, insert into database
        if len(data1) == 0:
            InsertData(conn, idCam, numIn , numOut  , doorStatus)
        else:  
            UpdateData(conn, idCam, numIn , numOut ,  doorStatus)
