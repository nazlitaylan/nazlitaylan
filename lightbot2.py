    elif komut== "^":
        if yon == 0: #if we were facing north
            if y < maxy: # check we are not at the top row
                y = y+1
        elif yon == 1: #if we are facing east
            if x < maxX: #check we are not at the last column
                x = x+1
        elif yon == 2: #if we are facing south
            if y>0: #check we are not at the bottom row
                y = y-1
        elif yon == 3: #if we are facing west
            if x>0: #check we are not at the first column
                x = x-1
                
    elif komut== "*":
        if yon == 0: #if we were facing north
            if y<maxy: 
                if abs(heightDifferenceForward()) == 1: #that might be -1 as well, it would jump down 
                    y = y+1
        elif yon == 1: #if we are facing east
            if x < maxX: #check we are not at the last column
                if abs(heightDifferenceForward()) == 1:
                    x = x+1
        elif yon == 2: #if we are facing south
            if y>0: #check we are not at the bottom row
                if abs(heightDifferenceForward()) == 1:
                     y = y-1
        elif yon == 3:
            if x>0: # check that we are not at the leftmost column
                if abs(heightDifferenceForward()) == 1: 
                    x = x-1 
                
    elif komut == "@":
        #if ( isBlue[x][y] ):     #this is same as checking ==True
        if ( isBlue[x][y]  == True ):
            print ("I am swithching on or off")
            #isOn[x][y] = not isOn[x][y]
            if ( isOn[x][y]== True):
                isOn[x][y]= False
            else:
                isOn[x][y] = True
        else:
            print("You are trying to light up a gray box. I can't do it")
    
    elif komut != "q":
        print("This command is not known")
        
print ("As I exit now, my orientation is", direction[yon])