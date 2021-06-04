import socket
import pickle
from time import sleep 

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 1235))

name = input("Enter your name : ")
c.send(bytes(name, 'utf-8'))

if(pickle.loads(c.recv(50))== 'Start'):
    while True:
        msg1 = int(input("Enter the number of straight going cars : "))
        msg2 = int(input("Enter the number of right going cars : "))

        if(msg1 == (-1) and msg2 ==(-1) ):
            c.send(pickle.dumps("end"))
            break
        else:
            sleep(0.1)
            c.send(pickle.dumps(msg1))
            sleep(0.1)
            c.send(pickle.dumps(msg2))

