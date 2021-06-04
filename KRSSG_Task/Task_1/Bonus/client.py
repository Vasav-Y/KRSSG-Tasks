import socket
import pickle
from time import sleep

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 1243))

name = input("Enter your name : ")
c.send(bytes(name, 'utf-8'))

print(pickle.loads(c.recv(300)))
end = "Thanks!"
while True:
    msg1 = int(input("Enter the number of players : "))
    msg2 = int(input("Enter the number of rounds after which the score is displayed : "))

    if((msg2 % msg1) == 0):
        print("Invalid Entry!")
        print("Number of rounds should not be divisible by number of players")
        continue
    else:
        c.send(pickle.dumps(msg1))
        sleep(0.2)
        c.send(pickle.dumps(msg2))
        print(pickle.loads(c.recv(300)))
        break