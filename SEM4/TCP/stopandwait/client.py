#20PW14.receiver.py
import socket

s = socket.socket()
host = socket.gethostname()
port = 65456

s.bind((host, port))
s.listen(5)
c, addr = s.accept()

arrival = ['0', '1', '0', '1', '0', '1']
rn = 0
iteration = 0
while (rn < len(arrival)):
    frame = c.recv(1).decode()
    print(frame)
    rn += 1
    iteration += 1
    if rn < len(arrival):
        print(f"Sending ACK {arrival[rn]}...")
        if iteration != 2 and iteration != 5:
            c.send(arrival[rn].encode())
    else:
        break
c.close()