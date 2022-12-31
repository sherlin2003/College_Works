import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',6000))
file_name="op"
data,address=s.recvfrom(1024)
f=open(file_name,'wb')
f.write(data)
f.close()
s.close()
