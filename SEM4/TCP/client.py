

import socket
c = socket.socket()
try:
    c.connect((socket.gethostname(),9999))
    name = input("Enter your name: ")
    c.send(name.encode())
    while True:
        s = input("Enter your message: ")
        c.send(s.encode())
        reply = c.recv(1024).decode()
        print(f"Server replied: {reply}")
        if reply == "Goodbye":
            break
    c.close() 
except ConnectionRefusedError:
    print("No connection could be made because the target machine actively refused it")

