import math
from socket import *

server = socket()
server.bind(('localhost', 12345))
server.listen(1)
client, address = server.accept()

def fragmentation(packetSize, networks, mtu):
    for i in range(len(mtu)):
        if packetSize > mtu[i]:
            size = packetSize - 20
            mtuSize = mtu[i] - 20
            while(mtuSize % 8 != 0):
                mtuSize -= 1
            fragNos = math.ceil(size/mtuSize)
            print("\nFragments count: ", fragNos)
            sizeArr = []
            while(True):
                if size > mtuSize:
                    sizeArr.append(mtuSize)
                    size -= mtuSize
                else:
                    sizeArr.append(size)
                    break
            offset = 0
            # print(sizeArr)
            print("\nID\tHLEN\tDLEN\tOFFSET\tM\tD\tR\n")
            for x in range(len(sizeArr)):
                M = 1
                if(x == len(sizeArr)-1):
                    M = 0
                print('X', '\t', 20, '\t', sizeArr[x], '\t', offset, '\t', M, '\t', 0, '\t', 0)
                offset = offset + mtuSize//8
            packetSize = mtu[i]
            

while True:
    info = client.recv(1024).decode().split(',')
    # print(info)
    packetSize = int(info[0])
    networks = int(info[1])
    mtu = list(map(int, info[2:]))
    # print(packetSize, networks, mtu)
    fragmentation(packetSize, networks, mtu)
    break
    