import socket
s = socket.socket()
host = socket.gethostname() 

port = 12345
print('SERVER '+host+'CONNECTED')
s.connect((host, port))
msg = ''
recc = ''
flag = 0
while(flag == 0):
    msg = input("enter the msg : ")
    s.send(bytes(msg,"utf-8"))
    recc = s.recv(1024).decode()
    print(recc)
    if(recc == 'eyB'):
        flag = 1

#print(msg.decode("utf-8"))
s.close()
