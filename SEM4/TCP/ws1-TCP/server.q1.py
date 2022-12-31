
import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)
while True:
    c, addr=s.accept()
    st=c.recv(1024).decode()
    if(st!='bye'):
         c.send(bytes('ok','utf-8'))
       
    else:
        c.send(bytes('BYE','utf-8'))
        c.close()
