import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    myname = client.recv(1024)
    print(myname.decode())

    client.send((20171514).to_bytes(4, 'big'))

    client.close()