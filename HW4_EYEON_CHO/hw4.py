import mimetypes
from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

msg1 = 'HTTP/1.1 200 OK\r\n'
msg2 = 'Context-Type: '
msg3 = '\r\n'
msg4 = 'HTTP/1.1 404 Not Found\r\n'
msg5 = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
msg6 = '<BODY>Not Found</BODY></HTML>'

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    decoded = data.decode()
    req = decoded.split('\r\n')
    req_info = req[0].split(' ')
    req_info = req_info[1][1:]

    if req_info == 'index.html':
        f = open('./index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'
        c.send(msg1.encode())
        msg = msg2 + mimeType + msg3
        c.send(msg.encode())
        c.send(msg3.encode())
        data = f.read()
        c.send(data.encode('euc-kr'))
    
    elif req_info == 'iot.png':
        f = open('./iot.png', 'rb')
        mimeType = 'image/png'
        c.send(msg1.encode())
        msg = msg2 + mimeType + msg3
        c.send(msg.encode())
        c.send(msg3.encode())
        data = f.read()
        c.send(data)
    
    elif req_info == 'favicon.ico':
        f = open('./favicon.ico', 'rb')
        mimeType = 'image/x-icon'
        c.send(msg1.encode())
        msg = msg2 + mimeType + msg3
        c.send(msg.encode())
        c.send(msg3.encode())
        data = f.read()
        c.send(data)

    else:
        c.send(msg4.encode())
        c.send(msg3.encode())
        c.send(msg5.encode())
        c.send(msg6.encode())
    
    c.close()