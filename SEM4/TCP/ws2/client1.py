import socket
import time

host = "localhost"
port = 5454
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    data_c = input("Client: ")
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.sendto(bytes(data_c, 'utf-8'),(host,port))    #send message
    c.close
   # time.sleep()



    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.bind((host, port))
    print("Server: " + c.recv(1024).decode('utf-8'))    # waiting for acknowledgment
    c.close
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    time.sleep(.1)