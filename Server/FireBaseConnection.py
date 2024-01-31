# Link: https://projectcameradata-default-rtdb.asia-southeast1.firebasedatabase.app
import firebase_admin
from firebase_admin import db, credentials

# Authenticate to firebase
cred = credentials.Certificate("D:\Document\Year5\Project3\Data-Processing\Server\credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://projectcameradata-default-rtdb.asia-southeast1.firebasedatabase.app"})

# Initialize data from camera with key is idCam
def InsertData(idCam, numIn, numOut, doorStatus):
    data = {    "numIn": numIn, 
                "numOut": numOut,
                "doorStatus": doorStatus
            }
    ref = db.reference('/')
    ref.child(idCam).set(data)

# Update Camera Info to Database
def UpdateData(idCam, numIn, numOut, doorStatus):
    data = {    "numIn": numIn, 
                "numOut": numOut,
                "doorStatus": doorStatus
            }
    ref = db.reference('/'+idCam)
    ref.update(data)
    
def UpdateCamStatus(idCam, camStatus):
    ref = db.reference('/'+idCam)
    ref.update({"camStatus":camStatus})

def getDataByID(idCam):
    ref = db.reference('/'+idCam)
    data = ref.get()
    return data
