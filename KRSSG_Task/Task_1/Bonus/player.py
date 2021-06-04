import socket
import pickle

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 1243))
card = []
name = input("Enter your name : ")
c.send(bytes(name, 'utf-8'))

print(pickle.loads(c.recv(300)))

while True:
    msg = pickle.loads(c.recv(300))
    if not msg:
        continue
    if (type(msg) == str):
        print(msg)
    elif msg:
        card = [msg[0], msg[1], msg[2]]
        print("Cards Received ", card)
        # Converting number on cards to 1-13 for player
        for i in range (3):
            if (card[i] <=13):
                pass

            elif(card[i] >13 and card[i] <=26):
                if(card[i] % 13 == 0):
                    card[i] = 13
                else:
                    card[i] = card[i] %13

            elif(card[i] >26 and card[i] <=39):
                if(card[i] % 13 == 0):
                    card[i] = 13
                else:
                    card[i] = card[i] %13

            elif(card[i] >39 and card[i] <=52):
                if(card[i] % 13 == 0):
                    card[i] = 13
                else:
                    card[i] = card[i] %13
        print("Cards in (1-13): ",card)
        #Finding the card with maximum number for the player 1
        if(card[0] > card[1]):
            p_1 = card[0]
        else:
            p_1 = card[1]

        if (p_1>card[2]):
            p1 = p_1
        else:
            p1 = card[2]

        print("Card with maximum value: ",p1,"\n")
        c.send(pickle.dumps(p1))

                