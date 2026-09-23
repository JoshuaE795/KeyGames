# SETUP
# ---------------------------------------------------------------------------------------------------------
import turtle
from time import sleep
from random import choice
import os
import sys

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Orangutan OS")
trtl = turtle.Turtle(visible=False)
trtl.pencolor("white")
helper = turtle.Turtle(visible=False)
helper.pencolor("white")
written = ""


def get_resource_path(relative_path):
    try:base_path = sys._MEIPASS
    except Exception:base_path = os.path.dirname(__file__)
    path = os.path.join(base_path, relative_path)
    if os.path.exists(path):
        return path
    return os.path.join(os.path.dirname(base_path), relative_path)


text_file_path = get_resource_path("typingtestparagrpahs.txt")
if not os.path.exists(text_file_path):
    text_file_path = get_resource_path("typingtestparagraphs.txt")

with open(text_file_path, 'r') as file:
    content = file.read()
    
# Paragraphs from https://randomwordgenerator.com/paragraph.php
bank = list(set(content.split('|')))
bank = [i+" " for i in bank]

true = choice(bank)
extra = [] # Remove the rearmost letters to make room for the newest ones so that the written does not go offscreen
over = False
count = -1
helper.pu()
helper.goto(0, 260)
secs, mins, hrs = (00, 00, 00)
timer = turtle.Turtle(visible=False)
timer.pu()
timer.goto(0,-200)
timer.pd()
timer.pencolor("white")
timer.write(f"Elapsed Time: 00:00:00", font=("Arial", 30, "bold"), align="center")
inputted = False
# ---------------------------------------------------------------------------------------------------------

# Divide each sentence into lines so the paragraph stays visible
# ---------------------------------------------------------------------------------------------------------
words = true.strip().split()
lines = []
current_line = ""

for word in words:
    if len(current_line) + len(word) + (1 if current_line else 0) <= 70:
        current_line += (" " if current_line else "") + word
    else:
        lines.append(current_line)
        current_line = word

if current_line:
    lines.append(current_line)

y = 200

for line in lines:
    y -= 20
    helper.goto(0, y)
    helper.write(line, align="center", font=("Arial", 15, "normal"))

# ---------------------------------------------------------------------------------------------------------

# DEFINE FUNCTIONS
# ---------------------------------------------------------------------------------------------------------
def check():
    global written, extra
    if ''.join(extra) + written[0:count+1] == true[0:count+1]: # To ensure accurate comparison, add the discarded letters to the written as well
        trtl.pencolor("lime")
    else:
        trtl.pencolor("red")
    if(len(written) > 31):
        extra.append(written[0])
        written = written[1:len(written)]


def stopwatch():
    global hrs, mins, secs, over, inputted
    sz = 0
    mz = 0
    hz = 0

    if (hrs == 59 and mins == 59 and secs == 59) or ''.join(extra) + written == true[0:-1]:
        over = True
    
    if not over and inputted:
        secs += 1

        if secs == 60:
            secs = 0
            sz = 0
            mins += 1

        if mins == 60:
            mins = 0
            mz = 0
            hrs += 1

        if len(str(secs)) == 2:
            sz = ""

        if len(str(mins)) == 2:
            mz = ""

        if len(str(hrs)) == 2:
            hz = ""

        timer.clear()
        timer.write(f"Elapsed Time: {hz}{hrs}:{mz}{mins}:{sz}{secs}", font=("Arial", 30, "bold"), align="center")    
    
    elif over:
        words = true[0:-1].replace(',','').split(" ")
        total = 60*hrs + mins + secs/60

        if total == 0:
            total = 1/60

        wn.textinput("Orangutan OS", f"You have a typing speed of about {round(len(words)/total, 1)} WPM")
        wn.bye()
        return
        
    trtl.getscreen().ontimer(stopwatch, 1000)


def char(char:str):
    global written, count, inputted
    inputted = True
    written += char
    count += 1
    check()
    trtl.clear()
    trtl.write(written, align="center", font=("Arial", 30, "normal"))


def dot(): char('.')


def comma():char(',')

def a():char('a')
def b():char('b')
def c():char('c')
def d():char('d')
def e():char('e')
def f():char('f')
def g():char('g')
def h():char('h')
def i():char('i')
def j():char('j')
def k():char('k')
def l():char('l')
def m():char('m')
def n():char('n')
def o():char('o')
def p():char('p')
def q():char('q')
def r():char('r')
def s():char('s')
def t():char('t')
def u():char('u')
def v():char('v')
def w():char('w')
def x():char('x')
def y():char('y')
def z():char('z')

def A():char('A')
def B():char('B')
def C():char('C')
def D():char('D')
def E():char('E')
def F():char('F')
def G():char('G')
def H():char('H')
def I():char('I')
def J():char('J')
def K():char('K')
def L():char('L')
def M():char('M')
def N():char('N')
def O():char('O')
def P():char('P')
def Q():char('Q')
def R():char('R')
def S():char('S')
def T():char('T')
def U():char('U')
def V():char('V')
def W():char('W')
def X():char('X')
def Y():char('Y')
def Z():char('Z')

def apostrophe():char("'")
def quote():char('"')
def open_parenthese():char('C')
def close_parenthese():char(')') 
def space():char(' ')
def question_mark():char('?')
def exclamation_mark():char('!')


def backspace():
    global written, count, inputted

    if not len(written) == 0:
        written = written[0:len(written)-1]
        count -= 1

    try: # Re-add old characters
        written = extra[-1] + written
        extra.pop()
    except:pass

    check()
    trtl.clear()
    trtl.write(written, align="center", font=("Arial", 30, "normal"))

# ---------------------------------------------------------------------------------------------------------


# ENABLE ONKEYPRESS
# ---------------------------------------------------------------------------------------------------------
wn.listen()

wn.ontimer(stopwatch, 1000)

wn.onkeypress(a,"a")
wn.onkeypress(b,"b")
wn.onkeypress(c,"c")
wn.onkeypress(d,"d")
wn.onkeypress(e,"e")
wn.onkeypress(f,"f")
wn.onkeypress(g,"g")
wn.onkeypress(h,"h")
wn.onkeypress(i,"i")
wn.onkeypress(j,"j")
wn.onkeypress(k,"k")
wn.onkeypress(l,"l")
wn.onkeypress(m,"m")
wn.onkeypress(n,"n")
wn.onkeypress(o,"o")
wn.onkeypress(p,"p")
wn.onkeypress(q,"q")
wn.onkeypress(r,"r")
wn.onkeypress(s,"s")
wn.onkeypress(t,"t")
wn.onkeypress(u,"u")
wn.onkeypress(v,"v")
wn.onkeypress(w,"w")
wn.onkeypress(x,"x")
wn.onkeypress(y,"y")
wn.onkeypress(z,"z")

wn.onkeypress(A,"A")
wn.onkeypress(B,"B")
wn.onkeypress(C,"C")
wn.onkeypress(D,"D")
wn.onkeypress(E,"E")
wn.onkeypress(F,"F")
wn.onkeypress(G,"G")
wn.onkeypress(H,"H")
wn.onkeypress(I,"I")
wn.onkeypress(J,"J")
wn.onkeypress(K,"K")
wn.onkeypress(L,"L")
wn.onkeypress(M,"M")
wn.onkeypress(N,"N")
wn.onkeypress(O,"O")
wn.onkeypress(P,"P")
wn.onkeypress(Q,"Q")
wn.onkeypress(R,"R")
wn.onkeypress(S,"S")
wn.onkeypress(T,"T")
wn.onkeypress(U,"U")
wn.onkeypress(V,"V")
wn.onkeypress(W,"W")
wn.onkeypress(X,"X")
wn.onkeypress(Y,"Y")
wn.onkeypress(Z,"Z")

wn.onkeypress(space, "space")
wn.onkeypress(backspace, "BackSpace")
wn.onkeypress(dot, ".")
wn.onkeypress(comma, ",")
wn.onkeypress(quote, '"')
wn.onkeypress(apostrophe, "'")
wn.onkeypress(open_parenthese, "(")
wn.onkeypress(close_parenthese, ")")
wn.onkeypress(question_mark, '?')
wn.onkeypress(exclamation_mark, '!')

# ---------------------------------------------------------------------------------------------------------

wn.mainloop()