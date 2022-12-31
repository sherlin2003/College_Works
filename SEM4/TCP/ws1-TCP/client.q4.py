import socket
s = socket.socket()
host = socket.gethostname() 
port = 12345
print(host)
s.connect((host, port))
s.send(b'Hi')
st1=s.recv(1024).decode()
print(st1)
#print(msg.decode("utf-8"))
s.close()
