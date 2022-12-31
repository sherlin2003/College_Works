import socket
s = socket.socket()
host = socket.gethostname()
print(host)
port = 12345
s.bind((host, port))
s.listen(5)
while True:
   c, addr = s.accept()
   print ('Got connection from', addr)
   c.send(b'Thank you for connecting')
   st= c.recv(1024).decode
   c.send(bytes(st,'utf-8'))  
 #c.send(bytes("Socket Programming in Python","utf-8 ")) 
c.close()

