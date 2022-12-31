import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',9999))
print("Server waiting")
while True :
   received = print("Client: " + s.recv(1024).decode('utf-8'))   #waiting to receive
s.close()
