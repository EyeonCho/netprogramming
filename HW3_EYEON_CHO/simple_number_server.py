from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 4444))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            data = data.decode()

            if data.find("+") != -1:
                data = data.split("+")
                val = str(float(data[0]) + float(data[1]))
            elif data.find("-") != -1:
                data = data.split("-")
                val = str(float(data[0]) - float(data[1]))
            elif data.find("*") != -1:
                data = data.split("*")
                val = str(float(data[0]) * float(data[1]))
            elif data.find("/") != -1:
                data = data.split("/")
                val = str(float(data[0]) / float(data[1]))
        except:
            client.send(b'Try again')
        else:
            client.send(val.encode())
            
client.close()