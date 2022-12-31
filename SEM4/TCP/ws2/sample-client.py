import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddr=('localhost',9999)
opt='y'
while opt=='y' or opt=='Y':
    data_c = input("Client: ")
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.sendto(bytes(data_c, 'utf-8'),serverAddr)    #send message
    op=input("Do you want to continue: ")
    opt=op

c.close()