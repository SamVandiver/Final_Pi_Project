import random
import socket
import sys
import codeGenLibrary as CODE
import classes
#   if you want to use a funtion in godeGenLibrary like generateCode() then do code.generateCode()

'''
# Set up a TCP/IP server
TCP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Bind the socket to server address and port 81
SERVER_ADDRESS = ('localhost', 81)
TCP_SOCKET.bind(SERVER_ADDRESS)
 
# Listen on port 81
TCP_SOCKET.listen(1)

while True:
    print("Waiting for connection")
    connection, client = TCP_SOCKET.accept()
 
    try:
        print(f"Connected to client IP: {client}")
         
        # Receive and print data 32 bytes at a time, as long as the client is sending something
        while True:
            data = connection.recv(32)
            print(f"Received data: {data}")
 
            if not data:
                break
 
    finally:
        connection.close()
'''
print(serial)
code = CODE.generateCode()
print(code)
