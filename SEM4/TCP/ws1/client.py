# -*- coding: utf-8 -*-
"""
client program
"""
import socket
s=socket.socket()
host='10.1.66.232' 
port=12345
print(host)
s.connect((host,port))
print(s.recv(1024).decode())
s.close()
