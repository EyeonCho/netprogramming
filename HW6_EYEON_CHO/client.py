from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET,  SOCK_DGRAM)

while True:
    msg = input('Enter the message ("send mboxID message" or "receive mboxId") : ')
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

    if data.decode() == 'quit':
        break