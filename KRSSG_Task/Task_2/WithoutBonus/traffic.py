t = int(input("Enter the number of time steps for which the cars will enter: "))
print(f"\nThe number of time steps for which the cars will enter: {t}")

hall = 0
input_list = []
car = []
carstot = [0,0,0,0,0,0,0,0]
j = 1
lanes = ['A', 'B', 'C', 'D']

'''All the states '''
states = [[0,1],[0,2],[0,7],[1,3],[1,4],[2,3],[2,5],[3,6],[4,5],[4,6],[5,7],[6,7]]

def PrintA(lane,x,y):
    if(x == 0 and y == 1):
        print(f"{lane} - go straight, go right ")
    elif( x== 0 or y == 0):
        print(f"{lane} - go straight")
    elif(x == 1 or y == 1):
        print(f"{lane} - go right ")
    else:
        print(f"{lane} - off ")

def PrintB(lane,x,y):
    if(x == 2 and y == 3):
        print(f"{lane} - go straight, go right ")
    elif( x== 2 or y == 2):
        print(f"{lane} - go straight")
    elif(x == 3 or y == 3):
        print(f"{lane} - go right ")
    else:
        print(f"{lane} - off ")

def PrintC(lane,x,y):
    if(x == 4 and y == 5):
        print(f"{lane} - go straight, go right ")
    elif( x== 4 or y == 4):
        print(f"{lane} - go straight")
    elif(x == 5 or y == 5):
        print(f"{lane} - go right ")
    else:
        print(f"{lane} - off ")

def PrintD(lane,x,y):
    if(x == 6 and y == 7):
        print(f"{lane} - go straight, go right ")
    elif( x== 6 or y == 6):
        print(f"{lane} - go straight")
    elif(x == 7 or y == 7):
        print(f"{lane} - go right ")
    else:
        print(f"{lane} - off ")

def UpdateCars(x,y):
    carstot[x] -= 1
    
    if (y != None):
        carstot[y] -= 1

    PrintA(lanes[0], x, y)
    PrintB(lanes[1], x, y)
    PrintC(lanes[2], x, y)
    PrintD(lanes[3], x, y)
    if(hall == 1):
        print(f"Output Queue : {carstot[0]} {carstot[1]} {carstot[2]} {carstot[3]} {carstot[4]} {carstot[5]} {carstot[6]} {carstot[7]}")
        print(f"\n Time Step: {j+1}\n")
        print(f"Input Queue : {carstot[0]} {carstot[1]} {carstot[2]} {carstot[3]} {carstot[4]} {carstot[5]} {carstot[6]} {carstot[7]}")

    
def NewState(states, index_car, no_index_car):
    global hall

    if(len(index_car) == 1):
        x = index_car[0]
        UpdateCars(x,None)
    
    maxcar = max(no_index_car)
    index_maxcar = no_index_car.index(maxcar)
    x = index_car[index_maxcar]

    counter = 0
    for state in states:
        if (state[0] == x):
            y = state[1]
            if y in index_car:
                counter = 1
                break
        elif(state[1] == x):
            if state[0] in states :
                x = state[0]
                y = state[1]
                counter = 1
                break
    
    if(counter == 1):
        return UpdateCars(x,y)
        
    else:
        no_index_car.remove(maxcar)
        index_car.remove(x)
        if(len(index_car) == 0 and sum(carstot) != 0):
            hall = 1
            for index, cars in enumerate(carstot):
                if cars != 0:
                    index_car.append(index)
                    no_index_car.append(cars)

            return NewState(states, index_car, no_index_car)

        if(sum(carstot) == 0):
            return
        else:
            return NewState(states, index_car, no_index_car)
        
        
            
    
def transition():
    print(f"Input Queue : {carstot[0]} {carstot[1]} {carstot[2]} {carstot[3]} {carstot[4]} {carstot[5]} {carstot[6]} {carstot[7]}")
    
    index_car = [] #stores index where car is present
    no_index_car = [] # stores number of car at that index

    for index, cars in enumerate(carstot):
        if cars != 0:
            index_car.append(index)
            no_index_car.append(cars)

    return NewState(states, index_car, no_index_car)

def output():
    global j, t
    print(f"Output Queue : {carstot[0]} {carstot[1]} {carstot[2]} {carstot[3]} {carstot[4]} {carstot[5]} {carstot[6]} {carstot[7]}")
    j += 1


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
    transition()
    output()

while(j >= t+1):
    print(f"\n Time Step: {j}\n")
    transition()
    print(f"Output Queue : {carstot[0]} {carstot[1]} {carstot[2]} {carstot[3]} {carstot[4]} {carstot[5]} {carstot[6]} {carstot[7]}")
    j += 1
    if(sum(carstot) == 0):
        print('Traffic Resolved : )')
        break


#There are total of 12 cases for clearing traffic
'''Which are as follows
(1)A straight, A right ->(0,1)
(2)A right, B right ->(1,3)
(3)A straight, B straight ->(0,2)
(4)A straight, D right ->(1,7)
(5)B straight, B right ->(2,3)
(6)B straight, C right ->(2,5)
(7)C straight, C right ->(4,5)
(8)C right, D right ->(5,7)
(9)C straight, D straight ->(5,6)
(10)C straight, A right ->(4,1)
(11)D straight, D right ->(6,7)
(12)D straight, B right ->(6,2)

if my FSM function calls a state say A straight and A right but the number of cars which want to go right from lane A so in this
case singlecars function will be called and a single car will be allowed to clear traffic
'''