
import socket
s=socket.socket()
s.connect((socket.gethostname(),65432))

while True:
    MSG=input(" please enter the message ")
    s.send(MSG.encode())
s.close()    
     
