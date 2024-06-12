import json
import requests
from tkinter import messagebox

from ShowMessage import *
from FileHandler import *

# Status: 0->1 : mat ket noi ; 1->0: Khoi phuc ket noi
global status
status = 0

url = 'https://service.vst.edu.vn/api/bus'

def CheckConnection():
    try:
        response = requests.get(url, timeout = 3)
        return True
    except:
        return False  
    
def SendDataToServer(dataToSend):
    global status
    if CheckConnection() : 
        if status == 1:
            status = 0
            Info = showMessage("Đã kết nối lại đường truyền mạng!", type = 'info', timeout=2500)
        
        json_dataToSend = json.dumps(dataToSend)
                
        #  Make Post request
        response = requests.post(url, json=json_dataToSend)
                
        # Check the response
        if response.status_code == 200:
            WriteToFile('Server has received data!')
        else:
            WriteToFile("Error:", response.status_code)
            WriteToFile(response.text)
    else :
        if status == 0:
            status = 1
            Warning = showMessage("Không thể kết nối đến Server! \n Vui lòng kiểm tra lại đường truyền mạng!", type = 'warning', timeout=2500)
        WriteToFile("Can not connect to server!")
    