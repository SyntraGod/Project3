import socket, ssl

from CameraData.GetCameraData import *
from datetime import datetime

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9999  # The port used by the server

def main():
    # Connect to server 
    clientSocket.connect((HOST, PORT))
    
    # Open Serial
    global ser
    initSerial()
    ser.open()  
    
    lastTime = round(time.time())
    
    while True:
        curtime = datetime.now()
        hour = curtime.hour
        min  = curtime.minute
        sec = curtime.second
        
        # Reset counter at 00:00:00
        if hour == 0 and min == 0 and sec == 0:
            resetCounter() 
        
        # Send data to server every 3 seconds
        cur = round(time.time())
        
        if(cur - lastTime >= 3):
            # dataToSend = '0001:10/1/0/1' 
            
            # Get data from camera 1 and camera 2 then send to Server  
            dataFromCam1 = getDataStream()
            clientSocket.sendall(dataFromCam1.encode())
            dataResponse = clientSocket.recv(1024).decode()
            print(f"Received response 1 {dataResponse!r}")
            
            time.sleep(0.1)
            
            dataFromCam2 = getDataStream2()
            clientSocket.sendall(dataFromCam2.encode())
            dataResponse = clientSocket.recv(1024).decode()
            print(f"Received response 2 {dataResponse!r}")
            
            lastTime = cur

    # ser.close()
    clientSocket.close()

if __name__ == '__main__':
    main()
    
    