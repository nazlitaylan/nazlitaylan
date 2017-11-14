# level 1 terrain : write column by column, ex: [ [0,1,0], [2,1,0] ] is a 2x3 terrain 
height = [[0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0]]
isBlue = [ [True,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,True] ]
isOn = [ [False,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,False,False], [False,False,False,False, True] ] 

# start by initializing the lightbot status variables
x = 0 #position of x-coordinate
y = 0 #position of y-coordinate
yon = 0 #which way out lbot is facing
direction = { 0: 'north', 1 : 'east', 2: 'south', 3: 'west' }

maxX = len(height)-1 #max possible value of the x coordinate
maxy = len(height[0])-1 #max possible value of the y coordinate

def heightDifferenceForward():
    """A function to compute the difference between the current box that the lightbot is occupying, and the box it is facing"""
    if yon == 0 and y<maxY:
        return height[x][y+1]-height[x][y]
    elif yon == 1 and x < maxX:
        return height[x+1][y]-height[x][y]
    elif yon == 2 and y>0:
        return height[x][y-1]-height[x][y]
    elif yon == 3 and x>0:
        return height[x-1][y]-height[x][y]
    return 0

komut = ""
while komut != "q" : #repeat as long as we don't get the quit command
    print("Enter a command for lbot")
    komut = input() 
    
    if komut== "<":
        print ('I am turning left')
        yon = (yon-1)%4
    
    elif komut== ">":
        print ('I am turning right')
        yon = (yon+1)%4