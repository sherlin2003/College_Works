import socket
import time

host = "localhost" 
port = 5454   
data_s = "ACKNOWLEDGMENT"


while 1:
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
   s.bind((host, port))    
   received = print("Client: " + s.recv(1024).decode('utf-8'))   #waiting to receive
   s.close
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   time.sleep(.1)



   s.sendto(bytes(data_s, 'utf-8'),(host,port))    #sending acknowledgment
   print("Server: " + data_s)
   s.close        # close out so that nothing sketchy happens 
   time.sleep(.1) # the delay keeps the binding from happening to quickly

