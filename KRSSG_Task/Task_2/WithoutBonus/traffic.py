import random

t = int(input("Enter the number of time steps for which the cars will enter: "))
print(f"\nThe number of time steps for which the cars will enter: {t}")

input_list = []
car = []
carstot = [0,0,0,0,0,0,0,0]
j = 1
lanes = ['A', 'B', 'C', 'D']

class TrafficResolve():
    global case
    @staticmethod
    def states():
        if(carstot[0]>=4):
            case = random.choice([1,3,4])
        elif(carstot[1]>=4):
            case = random.choice([1,2,10])
        elif(carstot[2]>=4):
            case = random.choice([3,5,6])
        elif(carstot[3]>=4):
            case = random.choice([2,5,12])
        elif(carstot[4]>=4):
            case = random.choice([7,9,10])
        elif(carstot[5]>=4):
            case = random.choice([6,7,8])
        elif(carstot[6]>=4):
            case = random.choice([9,11,12])
        elif(carstot[7]>=4):
            case = random.choice([4,8,11])
        else:
            case = random.randint(1, 12)

        if (case == 1):
            if(carstot[0] > 0 and carstot[1] > 0):
                Lane.LaneCars(lanes[0],'s')
                Lane.LaneCars(lanes[0],'r')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'n')
            else:
                TrafficResolve.SingleCars()

        elif(case == 2):
            if(carstot[1] > 0 and carstot[3] > 0):
                Lane.LaneCars(lanes[0], 'r')
                Lane.LaneCars(lanes[1], 'r')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'n')
            else:
                TrafficResolve.SingleCars()

        elif(case == 3):
            if(carstot[0] > 0 and carstot[2] > 0):
                Lane.LaneCars(lanes[0], 's')
                Lane.LaneCars(lanes[1], 's')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'n')
            else:
                TrafficResolve.SingleCars()

        elif (case == 4):
            if(carstot[0] > 0 and carstot[7] > 0):
                Lane.LaneCars(lanes[0],'s')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'r')
            else:
                TrafficResolve.SingleCars()

        elif (case == 5):
            if(carstot[2] > 0 and carstot[3] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 's')
                Lane.LaneCars(lanes[1], 'r')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'n')
            else:
                TrafficResolve.SingleCars()

        elif(case == 6):
            if(carstot[2] > 0 and carstot[5] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 's')
                Lane.LaneCars(lanes[2], 'r')
                Lane.LaneCars(lanes[3], 'n')
            else:
                TrafficResolve.SingleCars()

        elif(case == 7):
            if(carstot[4] > 0 and carstot[5] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 's')
                Lane.LaneCars(lanes[2], 'r')
                Lane.LaneCars(lanes[3], 'n')
            else:
                TrafficResolve.SingleCars()

        elif (case == 8):
            if(carstot[5] > 0 and carstot[7] ):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'r')
                Lane.LaneCars(lanes[3], 'r')
            else:
                TrafficResolve.SingleCars()

        elif (case == 9):
            if(carstot[4] > 0 and carstot[6] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 's')
                Lane.LaneCars(lanes[3], 's')
            else:
                TrafficResolve.SingleCars()

        elif(case == 10):
            if(carstot[1] > 0 and carstot[4] > 0):
                Lane.LaneCars(lanes[0],'r')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 's')
                Lane.LaneCars(lanes[3], 'n')
            else:
                TrafficResolve.SingleCars()

        elif(case == 11):
            if(carstot[6] > 0 and carstot[7] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 's')
                Lane.LaneCars(lanes[3], 'r')
            else:
                TrafficResolve.SingleCars()

        elif (case == 12):
            if(carstot[3] > 0 and carstot[6] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'r')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 's')
            else:
                TrafficResolve.SingleCars()
    @staticmethod
    def SingleCars():

            if(carstot[0] > 0):
                Lane.LaneCars(lanes[0],'s')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'n')
            elif(carstot[1] > 0):
                Lane.LaneCars(lanes[0],'r')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'n')
            elif(carstot[2] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 's')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'n')
            elif(carstot[3] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'r')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'n')
            elif(carstot[4] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 's')
                Lane.LaneCars(lanes[3], 'n')
            elif(carstot[5] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'r')
                Lane.LaneCars(lanes[3], 'n')
            elif(carstot[6] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 's')
            elif(carstot[7] > 0):
                Lane.LaneCars(lanes[0],'n')
                Lane.LaneCars(lanes[1], 'n')
                Lane.LaneCars(lanes[2], 'n')
                Lane.LaneCars(lanes[3], 'r')


class Output:
    @staticmethod
    def sample():
        global j, t
        print(f"Output Queue : {carstot[0]} {carstot[1]} {carstot[2]} {carstot[3]} {carstot[4]} {carstot[5]} {carstot[6]} {carstot[7]}")
        j += 1

class Lane:
    @staticmethod
    def LaneCars(lane,dir):
        global carstot
        if(lane == 'A'):
            carstrt = carstot[0]
            carryt = carstot[1]
        elif(lane == 'B'):
            carstrt = carstot[2]
            carryt = carstot[3]
        elif(lane == 'C'):
            carstrt = carstot[4]
            carryt = carstot[5]
        elif(lane == 'D'):
            carstrt = carstot[6]
            carryt = carstot[7]

        if(dir == 's'):
            print(f"{lane} - go straight")
            carstrt -= 1
        elif(dir == 'r'):
            print(f"{lane} - go right")
            carryt -= 1
        elif(dir == 'n'):
            print(f"{lane} - off")
        
        if(lane == 'A'):
            carstot[0] = carstrt 
            carstot[1] = carryt
        elif(lane == 'B'):
            carstot[2] = carstrt 
            carstot[3] = carryt
        elif(lane == 'C'):
            carstot[4] = carstrt 
            carstot[5] = carryt
        elif(lane == 'D'):
            carstot[6] = carstrt 
            carstot[7] = carryt

class TrafficHandler:

    @staticmethod
    def trafficClear():
        print(f"Input Queue : {carstot[0]} {carstot[1]} {carstot[2]} {carstot[3]} {carstot[4]} {carstot[5]} {carstot[6]} {carstot[7]}")
        TrafficResolve.states()


with open("input.txt") as f:
    data = f.read()

for element in data:
    if element == ' ':
        continue
    if element == '\n':
        continue
    input_list.append(element)

for i in range(t):
    car = []
    for y in range (8):
        car.append(int(input_list[8*i+y]))
    
    for q in range(8):
        carstot[q] += car[q]

    print(f"\n Time Step: {j}\n")
    print(f"Input Line {i+1} : {car[0]} {car[1]} {car[2]} {car[3]} {car[4]} {car[5]} {car[6]} {car[7]}")
    TrafficHandler.trafficClear()
    Output.sample()

while(j >= t+1):
    print(f"\n Time Step: {j}\n")
    TrafficHandler.trafficClear()
    print(
        f"Output Queue : {carstot[0]} {carstot[1]} {carstot[2]} {carstot[3]} {carstot[4]} {carstot[5]} {carstot[6]} {carstot[7]}")
    j += 1
    if(carstot[0] == 0 and carstot[1] == 0 and carstot[2] == 0 and carstot[3] == 0 and carstot[4] == 0 and carstot[5] == 0 and carstot[6] == 0 and carstot[7] == 0):
        break
