import pickle
import socket
s = socket.socket()
host = socket.gethostname()
port = 65456
mydict={'a':1}
message=pickle.dumps(mydict)

s.bind((host,port))

s.listen(5)
while True:
        c, addr = s.accept()
        print(f"Got connection from {addr}")
        while True:
            c.send(message)
              
c.close()
