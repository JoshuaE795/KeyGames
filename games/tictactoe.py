import turtle
from time import sleep
wn = turtle.Screen()
one = turtle.Turtle(shape="square")
two = turtle.Turtle(shape="square")
three = turtle.Turtle(shape="square")
four = turtle.Turtle(shape="square")
five = turtle.Turtle(shape="square")
six = turtle.Turtle(shape="square")
seven = turtle.Turtle(shape="square")
eight = turtle.Turtle(shape="square")
nine = turtle.Turtle(shape="square")
grid = turtle.Turtle(visible=False)
idk = turtle.Turtle(visible=False)
grid.speed(0)
wn.bgcolor("black")
grid.pencolor("white")
turtles = [one,two,three,four,five,six,seven,eight,nine]
spaces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def checkWinner(m):# DEF FUNCTION WITH PARAMETER
    conditions = [spaces[0] == spaces[1] == spaces[2] == m,spaces[3] == spaces[4] == spaces[5] == m, spaces[6] == spaces[7] == spaces[8] == m, spaces[0] == spaces[3] == spaces[6] == m, spaces[1] == spaces[4] == spaces[7] == m, spaces[2] == spaces[5] == spaces[8] == m, spaces[0] == spaces[4] == spaces[8] == m, spaces[2] == spaces[4] == spaces[6] == m] 

    for condition in conditions:
        if condition: 
            sleep(0.1)
            wn.textinput("Orangutan OS", m+" wins!")
            wn.bye()

def checkDraw():
    if not checkWinner('X') and not checkWinner('O') and  ' ' not in spaces:
        sleep(0.1)
        wn.textinput("Oranguatn OS", "Game drawn...")
        wn.bye()

def check():
    checkWinner('X')
    checkWinner('O')
    checkDraw()
    idk.getscreen().ontimer(check, 1000)

for t in turtles:
    t.turtlesize(4.8)
    t.speed(0)
    t.pu()
    

one.goto(-100, 100)
two.goto(0, 100)
three.goto(100,100)
four.goto(-100, 0)
#five.goto(0,0) five doesnt need to anywhere
six.goto(100,0)
seven.goto(-100,-100)
eight.goto(0,-100)
nine.goto(100,-100)

count = 0

def drawline(x,y,facing):
    grid.pu()
    grid.goto(x,y)
    grid.pd()
    grid.seth(facing)
    grid.fd(300)

def onedraw(x,y):
    one.ht()
    global count
    if count%2 == 0:
        marker = 'X'
        
    else:
        marker = 'O'
    spaces[0] = marker
    one.pencolor("white")
    one.seth(270)
    one.fd(20)
    one.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
def twodraw(x,y):
    two.ht()
    global count
    if count%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    spaces[1] = marker
    two.pencolor("white")
    two.seth(270)
    two.fd(20)
    two.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
def threedraw(x,y):
    three.ht()
    global count
    if count%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    spaces[2] = marker
    three.seth(270)
    three.fd(20)
    three.pencolor("white")
    three.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
def fourdraw(x,y):
    four.ht()
    global count
    if count%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    spaces[3] = marker
    four.pencolor("white")
    four.seth(270)
    four.fd(20)
    four.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
def fivedraw(x,y):
    five.ht()
    global count
    if count%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    spaces[4] = marker
    five.pencolor("white")
    five.seth(270)
    five.fd(20)
    five.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
def sixdraw(x,y):
    six.ht()
    global count
    if count%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    spaces[5] = marker
    six.pencolor("white")
    six.seth(270)
    six.fd(20)
    six.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
def sevendraw(x,y):
    seven.ht()
    global count
    if count%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    spaces[6] = marker
    seven.pencolor("white")
    seven.seth(270)
    seven.fd(20)
    seven.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
def eightdraw(x,y):
    eight.ht()
    global count
    if count%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    spaces[7] = marker
    eight.pencolor("white")
    eight.seth(270)
    eight.fd(20)
    eight.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
def ninedraw(x,y):
    nine.ht()
    global count
    if count%2 == 0:
        marker = 'X'
    else:
        marker = 'O'
    spaces[8] = marker
    nine.pencolor("white")
    nine.seth(270)
    nine.fd(20)
    nine.write(marker, font=("Arial", 40, "bold"), align="center")
    count+=1
    
#draw grid
drawline(-50,150, 270)
drawline(-150,50, 0)
drawline(-150,-50, 0)
drawline(50, 150, 270)

wn.listen()

one.onclick(onedraw)
two.onclick(twodraw)
three.onclick(threedraw)
four.onclick(fourdraw)
five.onclick(fivedraw)
six.onclick(sixdraw)
seven.onclick(sevendraw)
eight.onclick(eightdraw)
nine.onclick(ninedraw)
wn.ontimer(check, 1000)

wn.mainloop()
