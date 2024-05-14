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
    # if no data:   data = CamData : idCam / 'No Data' (0001/No data)
    # else :        data = CamData: idCam / numIn / numOut / doorStatus/ camStatus
    # GPS Data:     GPSData = GPS:lat/long
    
# update passenger flow to db
def processData(dataPackage):
        
    label, dataStream = dataPackage.split(':')
    
    # Process GPS Data and update DB
    if(label == 'GPS'):
        if dataStream == 'NoData':
            lat = 'N/A'
            long = 'N/A'
            alt = 'N/A'
            date = ''
            time = ''
            spd = 0
            nav = 'N/A'
            UpdateGPSData(lat, long, alt, date, time, spd, nav)
        else :
            lat, long, alt, date, time, spd, nav = dataStream.split('/')
            UpdateGPSData(lat, long, alt, date, time, spd, nav)
    else:
        idCam, package = dataStream.split('/',1)
        
        # Check current camStatus: 0 is off, 1 is on
        if package == "NoData":
            UpdateCamStatus(idCam , 0)
        else :
            UpdateCamStatus(idCam, 1)
            numIn, numOut, doorStatus, camStatus = package.split('/')
            
            data1 = getDataByID(idCam)

            # if id is not available, insert into database
            if len(data1) == 0:
                InsertData(idCam, numIn , numOut  , doorStatus)
            else:  
                UpdateData(idCam, numIn , numOut ,  doorStatus)
