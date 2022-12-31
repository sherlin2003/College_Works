
from socket import *

ID = '1001100010011001'
R = '0'
DF = '0'
HOST = 'localhost'
PORT = 65000

packet = ID+'-'+R+'-'+DF+'-0-0-'+'1780'
with socket(AF_INET, SOCK_STREAM) as c:
    c.connect((HOST, PORT))
    c.send((packet + ' 2 1500 572').encode())