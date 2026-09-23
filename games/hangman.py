# import modules
from random import choice
from time import sleep
import turtle
import os
import sys


# function to display prompts easily
def state(string:str):
    # write and clear each substring of the prompt, 
    # extending it by one charcter each iteration to 
    # give the illusion of being "typed"
    s = "" 
    for i in string:
        s += i
        label.clear()
        label.write(s, align='center', font=("Arial", 24, "normal"))

# function to obtain the correct path when run as a script or as an app
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

'''
function to reveal the correct word upon game end in red or green 
depending on the result of the game
'''
def reveal_word(col:str):
    for i in range(len(blanks)):
        helper.goto(blanks[i] - 30, 10)
        helper.pd()
        helper.pencolor(col)
        helper.write(word[i], font=('Arial', 30, 'normal'))
        helper.pu()


def check(char:str):
    global fails, word, length, let

    string = ""
    for i in tried:
        if i in word:
            string += i
    equal = True
    for i in range(len(sorted(set([i for i in string])))):
        if sorted(set([i for i in string]))[i] != sorted(set([i for i in word]))[i]:
            equal = False

    if let and (not (equal and len(sorted(set([i for i in string]))) == len(sorted(set([i for i in word]))))) and fails != 6:
        let = False
        display.color('red')
        
        if True: # I ain't re-tabbing allat (insert speaking emojis) (insert fire emojis)
            stopper = 'continue'
            for i in tried:
                if char == i:
                    state("You have already tried that.")
                    stopper = 'stop'
            if stopper != 'stop':
                tried.append(char)
                if word.find(char) != -1:
                    state(f"{char.upper()} is a letter in this word.")
                    count = []
                    pos = 0
                    for i in word:
                        if word[pos] == char:
                            count.append(pos + 1)
                            for j in count:
                                helper.goto(blanks[pos] - 30, 10)
                                helper.write(char, font=('Arial', 30, 'normal'))
                        pos += 1
                else:
                    fails += 1
                    state(f"{char.upper()} is not a letter in this word.")
                    if fails == 1:
                        helper.seth(180)
                        helper.goto(350,280)
                        helper.pd()
                        helper.circle(10)
                        helper.pu()
                        helper.goto(420,280)
                        helper.write(char, font=('Arial', 15, 'normal'))
                    elif fails == 2:
                        helper.goto(350,260)
                        helper.pd()
                        helper.seth(270)
                        helper.fd(50)
                        helper.pu()
                        helper.goto(420,260)
                        helper.write(char, font=('Arial', 15, 'normal'))
                    elif fails == 3:
                        helper.goto(350,210)
                        helper.pd()
                        helper.rt(30)
                        helper.fd(30)
                        helper.pu()
                        helper.goto(420,240)
                        helper.write(char, font=('Arial', 15, 'normal'))
                    elif fails == 4:
                        helper.goto(350,210)
                        helper.seth(270)
                        helper.lt(30)
                        helper.pd()
                        helper.fd(30)
                        helper.pu()
                        helper.goto(420,220)
                        helper.write(char, font=('Arial', 15, 'normal'))
                    elif fails == 5:
                        helper.goto(350, 250)
                        helper.seth(270)
                        helper.rt(30)
                        helper.pd()
                        helper.fd(30)
                        helper.pu()
                        helper.goto(420,200)
                        helper.write(char, font=('Arial', 15, 'normal'))
                    else:
                        helper.pu()
                        helper.goto(420,180)
                        helper.write(char, font=('Arial', 15, 'normal'))
                        if fails == 6:
                            helper.goto(350, 250)
                            helper.seth(270)
                            helper.lt(30)
                            helper.pd()
                            helper.fd(30)
                            helper.pu()
                            label.pencolor("red")
                            state("You have run out of attempts.")
                            helper.pu()
                            helper.pencolor('red')
                            reveal_word('red')
                            state(f"The word was {word}")  
                            helper.pencolor('black')
                            display.color('gray')      
                    let = True
        let = True
        if fails != 6:
            display.color('lime')
    string = ""
    for i in tried:
        if i in word:
            string += i

    equal = True
    for i in range(len(sorted(set([i for i in string])))):
        if sorted(set([i for i in string]))[i] != sorted(set([i for i in word]))[i]:
            equal = False
    if equal and len(sorted(set([i for i in string]))) == len(sorted(set([i for i in word]))):
        reveal_word("lime")
        label.pencolor("lime")
        state("You win!")
        display.color('gray')
        helper.pencolor('black')


def a(x=None, y=None): check('a')
def b(x=None, y=None): check('b')
def c(x=None, y=None): check('c')
def d(x=None, y=None): check('d')
def e(x=None, y=None): check('e')
def f(x=None, y=None): check('f')
def g(x=None, y=None): check('g')
def h(x=None, y=None): check('h')
def i(x=None, y=None): check('i')
def j(x=None, y=None): check('j')
def k(x=None, y=None): check('k')
def l(x=None, y=None): check('l')
def m(x=None, y=None): check('m')
def n(x=None, y=None): check('n')
def o(x=None, y=None): check('o')
def p(x=None, y=None): check('p')
def q(x=None, y=None): check('q')
def r(x=None, y=None): check('r')
def s(x=None, y=None): check('s')
def t(x=None, y=None): check('t')
def u(x=None, y=None): check('u')
def v(x=None, y=None): check('v')
def w(x=None, y=None): check('w')
def x(x=None, y=None): check('x')
def y(x=None, y=None): check('y')
def z(x=None, y=None): check('z')

# setup turtle window
wn = turtle.Screen()
wn.title("Orangutan OS")

# instantiate turtles
helper = turtle.Turtle(visible=False)
label = turtle.Turtle(visible=False)
display = turtle.Turtle(shape='circle')

# window setup
wn.bgcolor('black')
wn.setup(width=1200, height=700)

# helper turtle setup
helper.pencolor('white')
helper.speed(0)
helper.pu()

# draw the "hangman" strikes UI
helper.goto(300,300)
helper.pd()
helper.fd(100)
helper.rt(90)
helper.fd(150)
helper.pu()
helper.goto(350,300)
helper.seth(270)
helper.pd()
helper.fd(20)
helper.pu()

# setup prompt writing turtle
label.pu()
label.goto(0, 250)
label.pencolor("white")

# setup input indicator turtle
display.pu()
display.goto(-500, 300)
display.color("red")



state("Welcome to Hangman!")




wn.addshape(resource_path("button.gif"))

# create a dictionary of turtles to represent each letter of the alphabet 
letters = {turtle.Turtle(shape="square"):i for i in "abcdefghijklmnopqrstuvwxyz"}
delta_x = 0
delta_y = 0
for i in letters.keys():
    # setup each turtle
    i.ht()
    i.speed(0)
    i.shape(resource_path("button.gif"))
    i.pencolor("black")
    i.pu()
    i.shapesize(0.1, 0.1)

    '''
    when the x position of turtle has been shifted enough times, 
    move it down a line and to the start so that the buttons do 
    not go off-screen
    '''
    if(delta_x > 1000): 
        delta_x = 0
        delta_y = -80
    
    # send the turtle to the appropriate coordinates
    i.goto(-490 + delta_x, -200 + delta_y)
    i.st()

    # write the corresponding letter for the turtle on the button it is displaying
    i.write(letters.get(i).upper(), align='center', font=("Arial", 24, "normal")) 
    i.goto(i.xcor(), i.ycor() + 12.5)
    
    delta_x += 80 # gap of 80 between each button

'''
select a word randomly from a file containing numerous words 
and ensure it is at least 9 letters in length
'''
text_file_path = resource_path("words.txt")
with open(text_file_path, 'r') as file:
    content = file.read()
word = choice(content.split(' ')) 
while len(word) < 9: 
    word = choice(content.split(' ')) 

# initialze variables
length = len(word)
fails = 0
blanks = []
tried = []

# setup helper for writing user guesses
helper.goto(25*(0 - length), 0)
helper.seth(0)
helper.pu()


for line in range(length):
    helper.pd()
    helper.fd(40)
    blanks.append(helper.xcor())
    helper.pu()
    helper.fd(10)
    

let = True
display.color('lime')


        


list(letters.keys())[0].onclick(a)
list(letters.keys())[1].onclick(b)
list(letters.keys())[2].onclick(c)
list(letters.keys())[3].onclick(d)
list(letters.keys())[4].onclick(e)
list(letters.keys())[5].onclick(f)
list(letters.keys())[6].onclick(g)
list(letters.keys())[7].onclick(h)
list(letters.keys())[8].onclick(i)
list(letters.keys())[9].onclick(j)
list(letters.keys())[10].onclick(k)
list(letters.keys())[11].onclick(l)
list(letters.keys())[12].onclick(m)
list(letters.keys())[13].onclick(n)
list(letters.keys())[14].onclick(o)
list(letters.keys())[15].onclick(p)
list(letters.keys())[16].onclick(q)
list(letters.keys())[17].onclick(r)
list(letters.keys())[18].onclick(s)
list(letters.keys())[19].onclick(t)
list(letters.keys())[20].onclick(u)
list(letters.keys())[21].onclick(v)
list(letters.keys())[22].onclick(w)
list(letters.keys())[23].onclick(x)
list(letters.keys())[24].onclick(y)
list(letters.keys())[25].onclick(z)

wn.listen()

wn.onkeypress(a, 'a')
wn.onkeypress(b, 'b')
wn.onkeypress(c, 'c')
wn.onkeypress(d, 'd')
wn.onkeypress(e, 'e')
wn.onkeypress(f, 'f')
wn.onkeypress(g, 'g')
wn.onkeypress(h, 'h')
wn.onkeypress(i, 'i')
wn.onkeypress(j, 'j')
wn.onkeypress(k, 'k')
wn.onkeypress(l, 'l')
wn.onkeypress(m, 'm')
wn.onkeypress(n, 'n')
wn.onkeypress(o, 'o')
wn.onkeypress(p, 'p')
wn.onkeypress(q, 'q')
wn.onkeypress(r, 'r')
wn.onkeypress(s, 's')
wn.onkeypress(t, 't')
wn.onkeypress(u, 'u')
wn.onkeypress(v, 'v')
wn.onkeypress(w, 'w')
wn.onkeypress(x, 'x')
wn.onkeypress(y, 'y')
wn.onkeypress(z, 'z')
''
wn.mainloop()
