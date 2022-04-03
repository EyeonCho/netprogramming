import socket
import random

def dataGen():
    return str(random.randint(40, 141)) + ',' + str(random.randint(2000, 6001)) + ',' + str(random.randint(1000, 4001))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9001))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Request from ', addr)
    data = str(dataGen())
    print(data)
    client.send(data.encode())
    client.close()