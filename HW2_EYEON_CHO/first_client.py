from http import client
from re import ASCII
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

sock.send('Cho Eui Yeon'.encode())

mybytes = sock.recv(1024)
mynumber = int.from_bytes(mybytes, 'big')
print(mynumber)

sock.close()
