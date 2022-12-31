import socket
s = socket.socket()
host = socket.gethostname() 
port = 12345
print(host)
s.connect((host, port))
inpt=''
while(inpt=='y'):
	inpt=input("Enter the string to be sent")
	s.send(bytes(inpt,'utf-8'))
print(s.recv(1024).decode())
#print(msg.decode("utf-8"))

s.close()

