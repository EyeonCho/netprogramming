from pydoc import cli
import socket
import random

def dataGen() :
    return str(random.randint(0, 41)) + ',' + str(random.randint(0, 71)) + ',' + str(random.randint(70, 151))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Request from ', addr)
    data = str(dataGen())
    print(data)
    client.send(data.encode())
    client.close()