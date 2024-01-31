from FireBaseConnection import *
import time


def initDB():
    data1 = getDataByID('0001')
    # if id is not available, insert into database
    if data1 is None:
        InsertData('0001', 0 , 0  , 1)
        
    data1 = getDataByID('0002')
    # if id is not available, insert into database
    if data1 is None:
        InsertData('0002', 0 , 0  , 1)
        

# Data Structure:
    # if no data:   data = idCam : 'No Data' (0001/No data)
    # else :        data = idCam :  numIn / numOut / doorStatus/ camStatus
# update passenger flow to db
def updateDataToDB(dataPackage):
        
    dataStream = dataPackage.split(':')
    idCam = dataStream[0]
    package = dataStream[1]
    
    # Check current camStatus: 0 is off, 1 is on
    if package == "NoData":
        UpdateCamStatus(idCam , 0)
    else :
        UpdateCamStatus(idCam, 1)
        data = package.split('/')
        numIn = int(data[0])
        numOut = int(data[1])
        doorStatus = int(data[2])
        
        data1 = getDataByID(idCam)

        # if id is not available, insert into database
        if len(data1) == 0:
            InsertData(idCam, numIn , numOut  , doorStatus)
        else:  
            UpdateData(idCam, numIn , numOut ,  doorStatus)
