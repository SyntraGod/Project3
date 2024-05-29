import json
import requests
from tkinter import messagebox

from FileHandler import *

url = 'https://service.vst.edu.vn/api/bus'

def CheckConnection():
    try:
        response = requests.get(url, timeout = 3)
        return True
    except requests.ConnectionError:
        return False  
    
def SendDataToServer(dataToSend):
    if CheckConnection() : 
        json_dataToSend = json.dumps(dataToSend)
                
        #  Make Post request
        response = requests.post(url, json=json_dataToSend)
                
        # Check the response
        if response.status_code == 200:
            WriteToFile('Server has received data!')
        else:
            WriteToFile("Error:", response.status_code)
            WriteToFile(response.text)
    else:
        Error = messagebox.showerror(title='LỖI', message="Không thể kết nối đến Server! \n Vui lòng kiểm tra lại đường truyền mạng!")
        WriteToFile("Can not connect to server!")
        raise
    