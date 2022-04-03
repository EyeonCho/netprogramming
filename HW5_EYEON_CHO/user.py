import socket
import datetime

now = datetime.datetime.now()

addr1 = ('localhost', 9000)
addr2 = ('localhost', 9001)

f = open("./data.txt", 'a', encoding='utf-8')

while True:
    try:
        user_input = str(input())
        if user_input == '1':
            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s1.connect(addr1)
            data = s1.recv(1024).decode()
            print('1: '+ data)
            data = list(data.split(','))
            print('2: '+ str(data))
            date = now.strftime("%a %b %d %X %Y: Device1: ")
            date = date + "Temp=" + data[0] + ', Humid=' + data[1] + ', Iilum=' + data[2] + '\n'
            print('3: '+ date)
            f.write(date)
            s1.close()


        elif user_input == '2':
            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2.connect(addr2)
            data = s2.recv(2048).decode()
            print('1: '+ data)
            data = list(data.split(','))
            print('2: '+ str(data))
            date = now.strftime("%a %b %d %X %Y: Device1: ")
            date = date + "Heartbeat=" + data[0] + ', Steps=' + data[1] + ', Cal=' + data[2] + '\n'
            print('1: '+ date)
            f.write(date)
            s2.close()


        elif user_input == 'quit':
            f.close()
            break

    except Exception as e:
        print(e)