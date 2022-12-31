import socket
import pickle

s = socket.socket()
host = socket.gethostname()
port = 65456

s.connect((host,port))

while True:
    recvd = s.recv(1024) 
    print(pickle.loads(recvd))
    break
s.close()
