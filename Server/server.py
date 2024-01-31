import socket

from threading import *
from DataProcessing import *

import time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9999  # Port to listen on (non-privileged ports are > 1023)
serverSocket.bind((HOST, PORT))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()
    
    def run(self):
        # get data from client
        while True:
            try:
                data = self.sock.recv(1024).decode()
                if not data:
                    break
                print('Client: ', data)
                updateDataToDB(data)
                
                response = 'Received'
                self.sock.sendall(response.encode())
                
            except ConnectionError:
                print("Client disconnected" )
                break

def main():
    serverSocket.listen(5)
    print(f'Server is listening on {HOST}:{PORT}')

    startTime = round(time.time())
    
    while True:
        clientSocket, address = serverSocket.accept()
        print(f'New connection: {address[0]}:{address[1]}')
        client(clientSocket, address)
        
if __name__ == '__main__':
    main()