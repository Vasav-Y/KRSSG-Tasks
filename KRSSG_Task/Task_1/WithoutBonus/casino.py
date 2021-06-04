import socket
import threading
import pickle
from numpy import random
import numpy as np
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(3)
print("\n*********Casino Server is Online********\n")

countIn = [0,0,0]
countFin = [0,0,0]
conn = []
count = 0
i = 0
t = []
cards = []
ran_cards = []
player = []
player_score = []
playerScore = []
val = []
name_client = []
rang = np.arange(1,53)

def cards_random():
    global rang
    global cards
    global ran_cards
    '''Generation of random numbers(distinct) and storing them in a list '''
    cards = []
    ran_cards = []
    for w in range (52):
        ran_cards.append(rang[w])

    for e in range (9):
        x = random.choice(ran_cards)
        cards.append(x)
        ran_cards.remove(x)

    print("Cards for this round : ",cards)
  
def score():
    global name_client
    global val
    global countIn
    global countFin
    countIn = [0,0,0]
    player_score = []

#handling all the cases which the server will face when card will be returned to it from the players
    max_val = max(val)
    for q in range (3):
        if (val[q] == max_val):
            countIn[q] +=1 

    for q in range (3):
        countFin[q] += countIn[q]

    for q in range (3):
        print(f"{name_client[q]}'s score of this round = {countIn[q]}")

    max_score = max(countIn)
    for q in range(3):
        if(countIn[q] == max_score):
            player_score.append(name_client[q])

    if(len(player_score)==1):
        print(f"{player_score[0]} is Winner of this round!")

    elif(len(player_score)>1):
        sent = "This round is a tie between"
        for r in range (len(player_score)):
            sent += f" {player_score[r]},"
        print(sent[:-1])

    if(round ==4):
        print("\n")
        for q in range (3):
            print(f"{name_client[q]}'s final score = {countFin[q]}")
        finalScore = max(countFin)
        for y in range(3):
            if(countFin[y] == finalScore):
                playerScore.append(name_client[y])

        if(len(playerScore)==1):
            statement = f"\n{playerScore[0]} is Winner of the game!"
            print(statement)
            for f in range (3):
                conn[f].send(pickle.dumps(statement))

        elif(len(playerScore)>1):
            fsent = "This game is a tie between"
            for u in range (len(playerScore)):
                fsent += f" {playerScore[u]},"
            fsent = fsent[:-1]
            print(fsent)
            for f in range (3):
                conn[f].send(pickle.dumps(fsent))

    val = []

def distribute(pink):
    global player
    global val
    global i
    if(i ==3):
        i = 0

    player = [cards[3*i], cards[3*i + 1] , cards[3*i +2]]
    pink.send(pickle.dumps(player))
    i+=1

    a = pickle.loads(pink.recv(300))
    val.append(a)
    
    if(i==3):
        print("Cards received from the players are :",val)
        score()

def threads():
    global t
    t = []

    t.append(threading.Thread(target=distribute, args=(conn[0],)))
    t[0].start()
    sleep(0.2)
    t.append(threading.Thread(target=distribute, args=(conn[1],)))
    t[1].start()
    sleep(0.2)
    t.append(threading.Thread(target=distribute, args=(conn[2],)))
    t[2].start()
    sleep(0.2)
    
print("Waiting for palyers to join the game.....\n")
while True:
    
    global clientSocket
    global round
    round = 0

    clientSocket, addr = s.accept()
    conn.append(clientSocket)
    name = clientSocket.recv(30).decode()
    name_client.append(name)
    print(f"{name} has joined the game from the address : {addr}")
    clientSocket.send(pickle.dumps("Hello Player"))
    count+=1
    if(count==3):
        for k in range(4):          
            round+=1
            print(f"\n***** Round-{round}*****\n")
            cards_random()
            threads()
            sleep(0.1)



    
    


