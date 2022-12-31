# -*- coding: utf-8 -*-
"""server program """
import socket
s=socket.socket()
host='10.1.66.232'
print(host)
port=12345
s.bind((host,port))
s.listen(5)
while True :
    c,addr=s.accept()
    print(" Got connection from ",addr)
    c.send(b" thank you for connecting")
c.close()
