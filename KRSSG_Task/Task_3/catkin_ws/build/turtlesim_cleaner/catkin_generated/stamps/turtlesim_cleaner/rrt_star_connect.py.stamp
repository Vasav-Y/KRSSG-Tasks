#!/usr/bin/env python3
import cv2
import math
import random
import time
import heapq
from time import sleep
import socket
import pickle

a = 30
l = 8
size = []
xSource = 0
ySource = 0
xDestination = 0
yDestination = 0
counter = 0
blocked = 0
listSourceNode = []
listDestinationNode = []
count = 0
Path = [] #contains coordinates of points in path which will be sent to turtle
Path_final = []
xSource =int(input("Enter the x coordinate of source : "))
ySource =int(input("Enter the y coordinate of source : "))
xDestination =int(input("Enter the x coordinate of destination : "))
yDestination =int(input("Enter the y coordinate of destination : "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1237))
s.listen(1)
print("Waiting for Turtle to join........\n\n")

#keeping x and y in the dimensions of the img
def valid(x, y):
    global size
    global Path_final

    if (x >= 0 and y >= 0) and (x <= size[1] and y <= size[0]):
        return 1
    else:
        return 0

# checks closest Node to random point
def closestNode(xRad, yRad, listNode):

    xClosestNode = None
    yClosestNode = None
    distanceClosestNode = 100000

    for i in listNode:

        distanceCurrentNode = math.sqrt(
            (xRad-i[1])**2 + (yRad-i[0])**2)

        if distanceCurrentNode < distanceClosestNode:
            distanceClosestNode = distanceCurrentNode
            xClosestNode = i[1]
            yClosestNode = i[0]

    # returning closest Node and its distance
    return [yClosestNode, xClosestNode, distanceClosestNode]

# checks if point is on obstacle
def notObstacle(y, x, img):

    if int(img.item(y, x, 0)) < 50 or int(img.item(y, x, 1)) < 50 or int(img.item(y, x, 2)) < 50:
        return 1
    else:
        return 0

# checks lowest cost in the region
def lowestCostNode(nodeTree, xProbableNode, yProbableNode, costNode):
    global size
    global a
    global l

    xvals = []
    yvals = []
    nodeDistance = None
    xParentNode = None
    yParentNode = None
    lcstNodeDistance = 100000
    probableRemaps = []

    # finding valid points to check in a*a (in sqaure region)
    for i in range(xProbableNode-a, xProbableNode+a):
        if i >= 0 and i < size[1]:
            xvals.append(i)
    for i in range(yProbableNode-a, yProbableNode+a):
        if i >= 0 and i < size[0]:
            yvals.append(i)

    # finding lowest cost node
    for y in yvals:

        for x in xvals:
            if x == xProbableNode and y == yProbableNode:
                continue
            if nodeTree[y][x] == 1:
                # adding nodes in region for future use, when checking if other point can be updated with new node
                probableRemaps.append([y, x])
                nodeDistance = math.sqrt(
                    (xProbableNode - x)*(xProbableNode-x) + (yProbableNode-y)*(yProbableNode-y)) + costNode[y][x]
                if nodeDistance < lcstNodeDistance:
                    lcstNodeDistance = nodeDistance
                    xParentNode = x
                    yParentNode = y

    # returning parent node and its distance, also nodes to check remapping
    return [yParentNode, xParentNode, lcstNodeDistance], probableRemaps


# checks for any obstacles
def notBlocked(ParentNode, x, y, img):

    flag = 1

    if x-ParentNode[1] > 0:
        step = 1
    # corrected if the path becomes vertical
    elif x == ParentNode[1]:
        for i in range(y, ParentNode[0]):
            if not notObstacle(i, x, img):
                return 0
        return 1
    else:
        step = -1

    return flag

# if any remapping is done, cost needs to be changed of all child, done it using bfs
def changeCost(parentNode, costNode, node):

    priorityQueue = []
    # creating a prirority queue
    heapq.heapify(priorityQueue)
    heapq.heappush(priorityQueue, [0, node])

    numberElementsPriority = [1]
    i = 0

    while numberElementsPriority[i]:

        for j in range(0, numberElementsPriority[i]):

            numberElementsPriority.append(0)
    
            a = heapq.heappop(priorityQueue)
            distanceParent = math.sqrt((a[1][0]-parentNode[a[1][0]][a[1][1]][0][0])**2+(a[1][1]-parentNode[a[1][0]][a[1][1]][0][1])**2)
            costNode[a[1][0]][a[1][1]] = costNode[parentNode[a[1][0]][a[1][1]]
                                                  [0][0]][parentNode[a[1][0]][a[1][1]][0][1]] + distanceParent

            for k in range(1, len(parentNode[a[1][0]][a[1][1]])):
                heapq.heappush(priorityQueue, [
                               i+1, [parentNode[a[1][0]][a[1][1]][k][0], parentNode[a[1][0]][a[1][1]][k][1]]])
                numberElementsPriority[i+1] += 1

        i += 1

# changes colors of pixel lying on path between two nodes to shade of blue
def changeColour(image, node1, node2):
    global Path

    xDisplacement = node1[1]-node2[1]
    if xDisplacement > 0:
        step = 1
    else:
        step = -1

    # changes colour while travelling in x direction
    for i in range(0, xDisplacement, step):
        k = math.floor((i*node1[0]+(xDisplacement-i)*node2[0])/(xDisplacement))
        image.itemset((k, node2[1]+i, 0), 255)
        image.itemset((k, node2[1]+i, 1), 0)
        image.itemset((k, node2[1]+i, 2), 255)

    yDisplacement = node1[0]-node2[0]
    if yDisplacement > 0:
        step = 1
    else:
        step = -1

    # changes colour while travelling in y direction
    for i in range(0, yDisplacement, step):
        j = math.floor((i*node1[1]+(yDisplacement-i)*node2[1])/(yDisplacement))
        image.itemset((node2[0]+i, j, 0), 255)
        image.itemset((node2[0]+i, j, 1), 0)
        image.itemset((node2[0]+i, j, 2), 255)


# same as change colour, just changes colour for total nodes generated
def treeColour(image, node1, node2):
    xDisplacement = node1[1]-node2[1]
    if xDisplacement > 0:
        step = 1
    else:
        step = -1

    for i in range(0, xDisplacement, step):
        k = math.floor((i*node1[0]+(xDisplacement-i)*node2[0])/(xDisplacement))
        image.itemset((k, node2[1]+i, 0), 193)
        image.itemset((k, node2[1]+i, 1), 182)
        image.itemset((k, node2[1]+i, 2), 255)

    yDisplacement = node1[0]-node2[0]
    if yDisplacement > 0:
        step = 1
    else:
        step = -1

    for i in range(0, yDisplacement, step):
        j = math.floor((i*node1[1]+(yDisplacement-i)*node2[1])/(yDisplacement))
        image.itemset((node2[0]+i, j, 0), 193)
        image.itemset((node2[0]+i, j, 1), 182)
        image.itemset((node2[0]+i, j, 2), 255)

# explores all the nodes of given tree using bfs and changes colour, similar implementation as updating cost of all childs
def exploreTree(image, parentNode, node):

    priorityQueue = []
    heapq.heapify(priorityQueue)
    heapq.heappush(priorityQueue, [0, node])
    numberElementsPriority = [1]
    i = 0
    while numberElementsPriority[i]:
        for j in range(0, numberElementsPriority[i]):
            numberElementsPriority.append(0)
            a = heapq.heappop(priorityQueue)

            for k in range(1, len(parentNode[a[1][0]][a[1][1]])):
                heapq.heappush(priorityQueue, [
                               i+1, [parentNode[a[1][0]][a[1][1]][k][0], parentNode[a[1][0]][a[1][1]][k][1]]])
                treeColour(image, a[1], [
                           parentNode[a[1][0]][a[1][1]][k][0], parentNode[a[1][0]][a[1][1]][k][1]])
                numberElementsPriority[i+1] += 1
        i += 1


def connectNodes(image, parentNode, node):
    # initialises parent node
    xNode = node[1]
    yNode = node[0]

    # provides two nodes for path colouring
    # print([yNode, xNode], parentNode[yNode][xNode][0])
    while [yNode, xNode] != parentNode[yNode][xNode][0]:
        changeColour(image, [yNode, xNode], [
                     parentNode[yNode][xNode][0][0], parentNode[yNode][xNode][0][1]])
        Path.append([xNode, yNode])
        Path.append([parentNode[yNode][xNode][0][1],parentNode[yNode][xNode][0][0]])
        [yNode, xNode] = [parentNode[yNode][xNode]
                          [0][0], parentNode[yNode][xNode][0][1]]
        # print([yNode, xNode], parentNode[yNode][xNode][0])
    '''IF want to see some points on Image they are here '''
    # for a in Path:
    #     cv2.circle(img,(a[0],a[1]), 2,(0,165,255),2)

# takes a step in direction and creates node on given tree
#and gives different colour to nodes of source tree and destination tree
def createNode(img, nodeTree, connectionTree, parentNode, costNode, listNode,count):
    global size
    global counter
    global blocked

    d = 0
    # loops run till generated radom point is not on a node
    while not d:
        xRad = random.randrange(0, size[1])
        yRad = random.randrange(0, size[0])

        ClosestNode = closestNode(xRad, yRad, listNode)
        # calculate the coordinates of probable node
        if ClosestNode[2] != 0:
            xProbableNode = ClosestNode[1] + int((xRad - ClosestNode[1])*l/ClosestNode[2])
            yProbableNode = ClosestNode[0] + int((yRad - ClosestNode[0])*l/ClosestNode[2])
        d = ClosestNode[2]

    # check if node inside image
    if valid(xProbableNode, yProbableNode):
        # check if node is not on obstacle
        if notObstacle(yProbableNode, xProbableNode, img):
            ParentNode, probableRemaps = lowestCostNode(
                nodeTree, xProbableNode, yProbableNode, costNode)
            # check if path between node and parent node is blocked
            if notBlocked(ParentNode, xProbableNode, yProbableNode, img):
                # update point to become node
                nodeTree[yProbableNode][xProbableNode] = 1
                if [ParentNode[0], ParentNode[1]] == [yProbableNode, xProbableNode]:
                    print('error')
                # counts total number of nodes created
                counter += 1
                # update parent node of new node
                parentNode[yProbableNode][xProbableNode][0] = [
                    ParentNode[0], ParentNode[1]]
                # add child to parent node
                parentNode[ParentNode[0]][ParentNode[1]].append(
                    [yProbableNode, xProbableNode])
                if(count == 0):
                	cv2.circle(img,(xProbableNode,yProbableNode), 2 ,(255,215,0),2)
                else:
                	cv2.circle(img,(xProbableNode,yProbableNode),2  ,(0,255,255),2)
                # append in node list of tree
                listNode.append([yProbableNode, xProbableNode])
                # update the cost
                costNode[yProbableNode][xProbableNode] = ParentNode[2]
                # remap tree
                remapTree(xProbableNode, yProbableNode,
                          parentNode, costNode, probableRemaps)
                # connect tree
                connected, availableNodes = connectTree(
                    xProbableNode, yProbableNode, connectionTree, img)
                return connected, availableNodes
            else:
                blocked += 1
        else:
            blocked += 1
    else:
        blocked += 1

    return 0, 0

# checks for any remapping required
def remapTree(xNewNode, yNewNode, parentNode, costNode, probableRemaps):

    # iterate over all possible remaps
    for node in probableRemaps:
        distanceNewNode = math.sqrt(
            (node[0]-yNewNode)*(node[0]-yNewNode) + (node[1]-xNewNode)*(node[1]-xNewNode))
        # change parent and update cost of all child if any remap found
        if costNode[yNewNode][xNewNode] + distanceNewNode < costNode[node[0]][node[1]]:
            for child in parentNode[parentNode[node[0]][node[1]][0][0]][parentNode[node[0]][node[1]][0][1]]:
                # removing remapped point from its earlier parent child
                if child[0] == node[0] and child[1] == node[1]:
                    del child
                    break
            # updating new parent
            parentNode[node[0]][node[1]][0] = [yNewNode, xNewNode]
            # adding child to new parent
            parentNode[yNewNode][xNewNode].append([node[0], node[1]])
            # change cost of all child
            changeCost(parentNode, costNode, node)

# checks for minimum distance between new node and other tree, return all possible connection
def connectTree(xNewNode, yNewNode, connectionTree, img):
    global size
    global counter
    global blocked

    availableNodes = []
    connected = 0
    nodeDistance = None
    # iterate in l*l square
    for i in range(xNewNode-l, xNewNode+l+1):
        if i >= 0 and i < size[1]:
            for j in range(yNewNode-l, yNewNode+l+1):
                if j >= 0 and j < size[0]:
                    # checks if points are nodes
                    if connectionTree[j][i] == 1:
                        nodeDistance = math.sqrt(
                            (xNewNode-i)**2+(yNewNode-j)**2)
                        # checks if node are within 1 step
                        if nodeDistance <= l:
                            if notBlocked([yNewNode, xNewNode], i, j, img):
                                # adds any available connection
                                availableNodes.append(
                                    [[yNewNode, xNewNode], [j, i], nodeDistance])
                                connected = 1
    return connected, availableNodes

# shows tree by changing colour


def showTree(img, parentNewNode, parentNode, costNewNode,  costNode, availableConnections, startNewPoint, startPoint):
    totalPathLength = 1000000
    joint = None
    pathLength = None
    # checks for best possible connection i.e shortest path
    for connection in availableConnections:
        pathLength = costNewNode[connection[0][0]][connection[0][1]] + costNode[connection[1][0]][connection[1][1]] + connection[2]
        if pathLength < totalPathLength:
            joint = connection

    # print(joint)
    pathImage = img

    # explores both tree
    exploreTree(pathImage, parentNewNode, startNewPoint)
    exploreTree(pathImage, parentNode, startPoint)
    # changes colour of portion through which trees connects
    treeColour(pathImage, joint[0], joint[1])

    # prints path of tree on which new node is generated
    connectNodes(pathImage, parentNewNode, joint[0])
    # prints path of other tree
    connectNodes(pathImage, parentNode, joint[1])
    # joins both tree
    changeColour(pathImage, joint[0], joint[1])
    Path.append([joint[0][1],joint[0][0]])
    Path.append([joint[1][1],joint[1][0]])

    Path.sort()
    for b in range (0, len(Path)):
        if((b + 1 ) < len(Path)):
            if(Path[b + 1][1]< Path[b][1] ):
                Path[b + 1][0] = Path[b][0]
                Path[b + 1][1] = Path[b][1]
            else:
                continue
    for a in Path:
        if a not in Path_final:
            Path_final.append(a)
    print(Path_final)


    turtle, address =  s.accept()
    print("Turle has joined")
    turtle.send(pickle.dumps(Path_final))

    cv2.namedWindow("window1")
    cv2.imshow('window1', pathImage)
    cv2.waitKey(0)

def main():
    global size
    global xSource
    global ySource
    global xDestination
    global yDestination
    global listSourceNode
    global listDestinationNode
    global img 

    img = cv2.imread("Images/img2.png")
    size.append(img.shape[0])
    size.append(img.shape[1])

    # keeps tracks of points which are node
    nodeSourceTree = [[0 for _ in range(size[1])] for _ in range(size[0])]
    nodeDestinationTree = [[0 for _ in range(size[1])] for _ in range(size[0])]

    parentSourceNode = [[[[y, x]]
                         for x in range(size[1])] for y in range(size[0])]
    parentDestinationNode = [[[[y, x]]
                              for x in range(size[1])] for y in range(size[0])]

    # cost array for source and destination tree nodes
    costSourceNode = [[100000 for _ in range(size[1])] for _ in range(size[0])]
    costDestinationNode = [
        [100000 for _ in range(size[1])] for _ in range(size[0])]

    # finding source points
    # sourceDestPoints(img)
    sourcePoint = [ySource, xSource]
    destinationPoint = [yDestination, xDestination]

    # initialises parent of source and node tree
    nodeSourceTree[sourcePoint[0]][sourcePoint[1]] = 1
    nodeDestinationTree[destinationPoint[0]][destinationPoint[1]] = 1

    # adding nodes to list
    listSourceNode.append([sourcePoint[0], sourcePoint[1]])
    listDestinationNode.append([destinationPoint[0], destinationPoint[1]])

    # cost of source nd destination are zero
    costSourceNode[sourcePoint[0]][sourcePoint[1]] = 0
    costDestinationNode[destinationPoint[0]][destinationPoint[1]] = 0

    # flag for tree are connected or not
    connected = 0
    # stores all the ways in which both tree can be connected
    availableConnections = None
    # stores total path length
    pathLength = None
    while not connected:
        # creating node on source tree
        connected, availableConnections = createNode(
            img, nodeSourceTree, nodeDestinationTree, parentSourceNode, costSourceNode, listSourceNode,0)
        if connected:
            # showing path if both trees are connected
            showTree(img, parentSourceNode, parentDestinationNode, costSourceNode,
                     costDestinationNode, availableConnections, sourcePoint, destinationPoint)
            break

        # creating node on destination tree
        connected, availableConnections = createNode(
            img, nodeDestinationTree, nodeSourceTree, parentDestinationNode, costDestinationNode, listDestinationNode,1)
        if connected:
            # showing path if both trees are connected
            showTree(img, parentDestinationNode, parentSourceNode, costDestinationNode,
                     costSourceNode, availableConnections, destinationPoint, sourcePoint)
            break

if __name__ == "__main__":
    main()
