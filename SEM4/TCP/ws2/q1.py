import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
file_name="swetha.txt"
f=open(file_name,"r")
data=f.read(1024)
s.sendto(bytes(data,"utf-8"),('localhost',6000))
s.close()
f.close()