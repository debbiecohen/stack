#“I hereby certify that this program is  solely the result of my own work and
#is in compliance with the Academic Integrity policy of the course syllabus.”

import Draw
import time
import random
Draw.setCanvasSize(725, 750)

#This function draws the small twinkle squares in the background
def drawStars(starsList):
    for star in starsList:
        if random.random()<.01:
            star[2]=not star[2]
        if star[2]==True:
            Draw.setColor("RED")
            Draw.filledRect(star[0], star[1], 10, 10)
            Draw.setColor("BLUE")
            Draw.filledRect(star[1], star[0], 10, 10)
            Draw.setColor("MAGENTA")
            Draw.filledRect(star[0]+75, star[1]+25, 10, 10)   
            Draw.setColor("GREEN2")
            Draw.filledRect(star[1]-100, star[0]-60, 10, 10)  
            Draw.setColor("CYAN3")
            Draw.filledRect(star[0], star[1]-25, 10, 10)     
            Draw.setColor("PURPLE1")
            Draw.filledRect(star[1], star[1]+60, 10, 10)                
                         
#this function draws the background of the play again screen
def drawCircles():
    circlesList=[[random.randint(0,720),random.randint(0,720)] for i in range(50)]
    for circle in circlesList:
        Draw.setColor("YELLOW")
        Draw.filledOval(circle[0], circle[1], 80, 80)

#this function draws the name of the game "Stack"
def stackName():
    Draw.setFontSize(90)
    Draw.setColor("RED")
    Draw.string("STACK", 190, 603)
    Draw.setColor("BLACK")
    Draw.string("STACK", 193, 606) 
    Draw.setColor("RED")
    Draw.string("STACK", 196, 609)
        
#These two following functions takes the last box from the stack list as a parameter and the speed of the boxes.
#These, set the coordinates of the new moving box to the top right or left corner mantaining the size of the last box in the stack.
#Since the stackList elements doesn't include the direction/speed of the box, this functions appends it to the end and returns what its going to be after the stackList[-1]
def StartBoxCoordsLeft(topBox,d):
    ans=[]
    for coord in topBox:
        ans.append([coord[0]-200,coord[1]-225])
    ans.append([d,d])
    return ans

def StartBoxCoordsRight(topBox,d):
    ans=[]
    for coord in topBox:
        ans.append([coord[0]+200,coord[1]-225])
    ans.append([-d,d])
    return ans

#This illustrates a simple function to draw a filled quadrilateral
def filledQuad(x1, y1, x2, y2, x3, y3, x4, y4):
    coords = [x1, y1, x2, y2, x3, y3, x4, y4]
    Draw.filledPolygon(coords)

#Function to move the box one step(d)
def movingBox(stackList,d): 
    #if it comes from the left and one of the coordinate reaches the limit, change the direction. -->comes from left
    if stackList[-1][-1]==[d,d] and stackList[-1][3][0]>475: 
        stackList[-1][-1][0]=-d
        stackList[-1][-1][1]=-d
    #elif it comes from the left and one of the coordinate reaches the limit, change the direction. -->comes from left
    elif stackList[-1][-1]==[-d,-d] and stackList[-1][3][0]<50: 
        stackList[-1][-1][0]=d
        stackList[-1][-1][1]=d
    #elif it comes from the right and one of the coordinate reaches the limit, change the direction. -->comes from right
    elif stackList[-1][-1]==[-d,d] and stackList[-1][3][0]<25: 
        stackList[-1][-1][0]=d
        stackList[-1][-1][1]=-d
    #if it comes from the left and one of the coordinate reaches the limit, change the direction. -->comes from right
    elif stackList[-1][-1]==[d,-d] and stackList[-1][3][0]>475: 
        stackList[-1][-1][0]=-d
        stackList[-1][-1][1]=d
    #the following loop adds to each of the coordinates of the moving box, d and depending on the direction set before, it will move.
    for i in range(7):
        dx = stackList[-1][-1][0]
        dy = stackList[-1][-1][1]
        stackList[-1][i][0] += dx
        stackList[-1][i][1] += dy

#Erases saved clicks just in case the user clicked before. 
def flushClicks():
    while Draw.mousePressed():
        Draw.mouseX()
        Draw.mouseY()
        
#Erases saved pressed keys just in case the user pressed a key during the game over screen 
def flushKeys():
    while Draw.hasNextKeyTyped():
        newKey = Draw.nextKeyTyped()  
        
# Function to draw each box in the stack --> loop and draw with different colors
# stackList[box][always from 0 to 6 (only 7 points per box)][0 or 1 (for x or y)]
def drawStack(stackList):
    color=0
    i=1
    for box in range (len(stackList)):
        #the following if statements are in order to change the color from dark to light and from loight to dark
        if color*17>=203: #203 because I didnt want it to get until white
            i=-1
        elif color*17==0:
            i=1
        Draw.setColor(Draw.color(255, color*17, color*17)) #REDS
        filledQuad(stackList[box][0][0], stackList[box][0][1],\
                   stackList[box][1][0], stackList[box][1][1],\
                   stackList[box][2][0], stackList[box][2][1],\
                   stackList[box][3][0], stackList[box][3][1])
        Draw.setColor(Draw.color(255-color*17, 255-color*17, 255)) #WHITE-->BLUE
        filledQuad(stackList[box][3][0], stackList[box][3][1],\
                   stackList[box][2][0], stackList[box][2][1],\
                   stackList[box][5][0], stackList[box][5][1],\
                   stackList[box][4][0], stackList[box][4][1])
        Draw.setColor(Draw.color(color*17, color*17, 255)) #BLUE-->LIGHT BLUE
        filledQuad(stackList[box][2][0], stackList[box][2][1],\
                   stackList[box][1][0], stackList[box][1][1],\
                   stackList[box][6][0], stackList[box][6][1],\
                   stackList[box][5][0], stackList[box][5][1])
        color+=i
        
#move the stack 25 down so the tower can always fit in the screen
def moveStack(stackList):
    for box in stackList:
        for point in box:
            point[1]+=25
            
#Draws the score in the screen, takes the value of count as a parameter          
def drawCount(count):
    Draw.setFontSize(100)
    Draw.setFontBold(True)    
    Draw.setColor("YELLOW")
    Draw.string(str(count),310,80)
    Draw.setColor("RED")
    Draw.string(str(count),315,77) 
    Draw.setColor("YELLOW")
    Draw.string(str(count),318,74)    

#Draws the flash everytime the box is stopped in the exact place of the stack. Takes the last box from the stacklist and the value of exact as paramater
def drawLight(topBox, exact):
    if exact:
        x=40 #Size of the flash
        Draw.setColor("WHITE")
        Draw.filledPolygon([topBox[4][0], topBox[4][1]-x, topBox[4][0]-x,\
                            topBox[4][1], topBox[5][0], topBox[5][1]+x, \
                            topBox[6][0]+x, topBox[6][1], topBox[6][0], \
                            topBox[6][1]-x, topBox[6][0], topBox[6][1], \
                            topBox[5][0], topBox[5][1], topBox[4][0], topBox[4][1]])
        
# This is the main function, it includes the game over part   
def playGame():
    d=1 #initial speed of the game
    Draw.setBackground("BLACK")
    gameNotOver=True
    count=0 #initial count of boxes
    #list of stars in the background
    starsList=[[random.randint(0,720),random.randint(0,720), False] for i in range(20)]
    #list of the boxes in the stack. Starts with the stable one and the first moving box
    stackList=[[[350,275], [450,375], [350,475], [250,375], [250,400], [350,500], [450,400]],\
               [[150,50], [250,150], [150,250], [50,150], [50,175], [150,275], [250,175], [d, d]]]
    #next line--> while True
    while gameNotOver:    
        exact=False      
        if Draw.hasNextKeyTyped(): #If the user presses any key
            Draw.nextKeyTyped() 
            #If boxes is the same exact place, change exact to True
            if (stackList[-1][5][0]==stackList[-2][2][0] and stackList[-1][4][0]==stackList[-2][3][0]) or \
               (stackList[-1][5][0]==stackList[-2][2][0] and stackList[-1][6][0]==stackList[-2][1][0]):
                exact=True 
            #If the box is originally from left
            if stackList[-1][-1][0]==stackList[-1][-1][1]: 
                #If boxes overlap (coming from left up)
                if stackList[-2][3][0]<stackList[-1][5][0]<stackList[-2][2][0] or \
                   (stackList[-1][5][0]==stackList[-2][2][0] and stackList[-1][4][0]==stackList[-2][3][0]):
                    moveStack(stackList)
                    #Next line--> What are the coordinates of the new stackList[-1], append them to stackList
                    stackList[-1]=[[stackList[-2][0][0],stackList[-2][0][1]-25],\
                               [stackList[-1][1][0], stackList[-1][1][1]],\
                               [stackList[-1][2][0], stackList[-1][2][1]],\
                               [stackList[-2][3][0],stackList[-2][3][1]-25],\
                               [stackList[-2][4][0], stackList[-2][4][1]-25],\
                               [stackList[-1][5][0], stackList[-1][5][1]],\
                               [stackList[-1][6][0], stackList[-1][6][1]]]                      
                    count+=1
                    #increase speed every 3 boxes
                    if count%3==0 and count>0:
                        d+=0.5
                    stackList.append(StartBoxCoordsRight(stackList[-1],d)) #stackList[-1] (the new box) will have same size than last box in the stacklist but other coordinates, therefore we append the StartBoxCoordsRight or Left depending on each case.
                #If boxes overlap in another way or the box in the exact position of stack
                elif stackList[-2][3][0]<stackList[-1][4][0]<stackList[-2][2][0] or \
                     (stackList[-1][5][0]==stackList[-2][2][0] and stackList[-1][4][0]==stackList[-2][3][0]):
                    moveStack(stackList)
                    #Next line--> What are the coordinates of the new stackList[-1], append them to stackList
                    stackList[-1]=[[stackList[-1][0][0], stackList[-1][0][1]],\
                               [stackList[-2][1][0], stackList[-2][1][1]-25],\
                               [stackList[-2][2][0], stackList[-2][2][1]-25],\
                               [stackList[-1][3][0], stackList[-1][3][1]],\
                               [stackList[-1][4][0], stackList[-1][4][1]],\
                               [stackList[-2][5][0], stackList[-2][5][1]-25],\
                               [stackList[-2][6][0], stackList[-2][6][1]-25]]
                    count+=1
                    #increase speed
                    if count%3==0 and count>0:
                        d+=0.5  
                    stackList.append(StartBoxCoordsRight(stackList[-1],d))
                else: #Boxes don't overlap
                    gameNotOver=False                    
            else: #If the box is originally from right
                #If boxes overlap
                if stackList[-2][2][0]<stackList[-1][5][0]<stackList[-2][1][0] or \
                   (stackList[-1][5][0]==stackList[-2][2][0] and stackList[-1][6][0]==stackList[-2][1][0]):
                    #Next line--> What are the coordinates of the new stackList[-1], append them to stackList
                    moveStack(stackList)
                    stackList[-1]=[[stackList[-2][0][0], stackList[-2][0][1]-25],\
                               [stackList[-2][1][0],stackList[-2][1][1]-25], \
                               [stackList[-1][2][0], stackList[-1][2][1]],\
                               [stackList[-1][3][0], stackList[-1][3][1]],\
                               [stackList[-1][4][0], stackList[-1][4][1]],\
                               [stackList[-1][5][0], stackList[-1][5][1]],\
                               [stackList[-2][6][0],stackList[-2][6][1]-25]]
                    count+=1
                    #increase speed
                    if count%3==0 and count>0:
                        d+=0.5  
                    stackList.append(StartBoxCoordsLeft(stackList[-1],d))
                #If boxes overlap in another way or the box is in the exact possition of stack (comes back)
                elif stackList[-2][2][0]<stackList[-1][6][0]<stackList[-2][1][0] or \
                    (stackList[-1][5][0]==stackList[-2][2][0] and stackList[-1][6][0]==stackList[-2][1][0]):
                    moveStack(stackList)
                    #Next line--> What are the coordinates of the new stackList[-1], append them to stackList
                    stackList[-1]=[[stackList[-1][0][0], stackList[-1][0][1]],\
                               [stackList[-1][1][0], stackList[-1][1][1]],\
                               [stackList[-2][2][0], stackList[-2][2][1]-25],\
                               [stackList[-2][3][0], stackList[-2][3][1]-25],\
                               [stackList[-2][4][0], stackList[-2][4][1]-25],\
                               [stackList[-2][5][0], stackList[-2][5][1]-25],\
                               [stackList[-1][6][0], stackList[-1][6][1]]]
                    count+=1
                    #increase speed
                    if count%3==0 and count>0:
                        d+=0.5   
                    stackList.append(StartBoxCoordsLeft(stackList[-1],d))
                else: #Boxes don't overlap
                    gameNotOver=False                     
        movingBox(stackList,d) #move box one step, takes the list of boxes and the speed of the movement as a parameter
        Draw.clear() #clear the canvas
        drawStars(starsList) #Draw the "moving background"
        drawStack(stackList) #Draw the new stack
        drawLight(stackList[-2], exact) #If the box was stopped in the exact place, Draw the flash
        drawCount(count) #Draw the score
        stackName()
        Draw.show() #show everything
    gameOver(count) #game over screen

#Function that shows the game over screen   
def gameOver(count):
    #Draws the moving string game over
    for i in range(4): 
        Draw.setColor(Draw.DARK_RED)
        Draw.string("GAME OVER", 80,200)
        Draw.show()
        time.sleep(.5)
        Draw.setColor("YELLOW")
        Draw.string("GAME OVER", 90,200)
        Draw.show()
        time.sleep(.5)
    Draw.clear() #clear canvas
    drawCircles()
    Draw.setBackground("RED")
    Draw.setColor(Draw.WHITE)
    Draw.filledRect(280,300,150,150) #White part of the play botton
    Draw.setColor("GREY") #grey 3D part of the botton
    Draw.filledPolygon([280,300,280,450,260,470,260,320])
    Draw.setColor("BLACK") 
    Draw.polygon([280,300,280,450,260,470,260,320]) #Outline of 3D white part of the botton
    Draw.filledPolygon([260,470,280,450,427,450,407,470]) #black 3D part of the botton   
    Draw.rect(280,300,150,150) #Outline of white part of the botton
    Draw.filledPolygon([310,320,405,375,310,430]) #triangle of play
    Draw.string("PLAY AGAIN", 90, 200)    
    Draw.setFontSize(50)
    Draw.string("YOUR SCORE WAS: "+ str(count), 100, 550)
    Draw.string("Can you do it better?...", 120,100)
    Draw.filledRect(310,625,75,75)
    #Following lines are the help botton drawing
    Draw.setColor("WHITE")
    Draw.string("?", 335,640)
    Draw.setFontSize(15)
    Draw.string("HELP", 330,630)
    Draw.show()
    flushClicks()#erases saved clicks just in case the user clicked before
    #If user clicks in the "play botton", play again
    while True:
        if Draw.mousePressed():
            playX=Draw.mouseX()
            playY=Draw.mouseY()
            #if the user press the play botton, play again
            if playX> 280 and playX<430 and playY>300 and playY<450:
                flushKeys()
                playGame()
            #if the user press the help botton, show the basic instructions
            if playX> 310 and playX<385 and playY>625 and playY<700:
                Draw.setColor("WHITE")
                Draw.filledRect(240,608,210,138)
                Draw.setColor("BLACK")
                Draw.string("Stack up the blocks \nas high as you can!\n\nPress any key to stop\nthe boxes.\n\nWARNING!: DO NOT HOLD \nTHE KEY.", 252,610)
                
#Calling of the main function          
playGame() 