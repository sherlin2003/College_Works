
from socket import *
HOST = 'localhost'
PORT = 65000
ID = '1001100010011001'
R = '0'
DF = '0'

def fragment(datagram, mtu):
    datagramSize = int(datagram.split('-')[-1])+20
    offset = int(datagram.split('-')[-2])
    initM =  datagram.split('-')[-3]
    if datagramSize <= mtu:
        print([datagram])
        return [datagram]
    fragments = list()
    print('Fragmenting packet of size:', datagramSize)
    total_data_len = datagramSize-20
    data_len = mtu-20
    data_len = (data_len//8)*8
    M='1'
    while total_data_len >0:
        fragment = ID+'-'+R+'-'+DF+'-'
        fragOff = offset//8
        offset += data_len
        fragment += M+'-'+ str(fragOff) + '-'+ str(data_len)
        total_data_len -= data_len;
        if total_data_len <= data_len:
            M= initM
            data_len = total_data_len
        fragments.append(fragment)   
    print(fragments)
    return fragments

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode().split(' ')
            if data!=['']:
                fragments=[]
                print(data)
                fragments.append(data[0])
                n = int(data[1])
                mtu = [int(x) for x in data[2:2+n]]
                for i in range(len(mtu)):
                    fragmentsCopy=[]
                    for j in range(len(fragments)):
                        fragmentsCopy.append(fragments[j])
                    fragments = []
                    for j in range(len(fragmentsCopy)):
                        fragments += fragment(fragmentsCopy[j], mtu[i])
                print(fragments)
