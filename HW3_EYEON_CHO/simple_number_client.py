from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 4444))

while True:
    msg = input('Calc Input : ')
    if msg == 'q':
        break
    s.send(msg.encode())

    print('Received message :', msg)
    print('Result : {:.1f}'.format(float(s.recv(1024).decode())))

s.close()