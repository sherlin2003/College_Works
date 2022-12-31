"""Q1-server"""
import socket
s=socket.socket()
host=socket.gethostname()
s.bind((host,65432))
s.listen(1)
while True :
        c,addr=s.accept()
        print(" Got connection from ",addr)
s.close()
