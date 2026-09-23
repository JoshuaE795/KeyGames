import turtle
from random import choice, sample
from time import sleep
import os
import sys
wn = turtle.Screen()
wn.bgcolor("black")
trtl = turtle.Turtle(visible=False)
trtl.pencolor("white")
helper = turtle.Turtle(visible=False)
helper.pencolor("white")
timer = turtle.Turtle(visible=False)
timer.pencolor("white")
times = 0
written = ""
#bank = ['bioluminescent', 'incendiary', 'neutralization', 'groveling', 'tyrannical', 'flamboyant', 'slovakian','affiliation', 'polysaccharide', 'deoxyribonucleic', 'condensation', 'triphosphate', 'generation', 'anthropomorphization','hereditary', 'superfluous', 'collaborative', 'cytokinesis', 'encompass', 'penultimate', 'ludicrous', 'excellent', 'boisterous', 'camouflage', 'dandelion', 'celebration' ,'outrageous', 'impossible']
#bank = ["hello", "crowd", "flint", "smash", "cross"]

def get_resource_path(relative_path):
    try:base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

text_file_path = get_resource_path("typinggamewords.txt")
with open(text_file_path, 'r') as file:
    content = file.read()

bigbank = [i.strip() for i in content.split() if i.isalpha() and len(i) >= 8]
bank = sample(bigbank, 30)

over = False
count = 0
timeLeft = 5
true = bank[count]
helper.pu()
helper.goto(0, 200)
helper.write(true, align="center", font=("Arial", 30, "normal"))
timer.pu()
timer.goto(0,-200)
timer.write("Time remaining: "+str(timeLeft), font=("Arial", 30, "bold"), align="center")

def countdown():
    global timeLeft, over
    if not over:
        timeLeft -= 1
        timer.clear()
        timer.write("Time remaining: "+str(timeLeft), font=("Arial", 30, "bold"), align="center")
    if timeLeft <= 0:
        wn.textinput("Orangutan OS", "Too slow. ")
        wn.bye()
        over = True
    trtl.getscreen().ontimer(countdown, 1000)


def check() :
    global count, true, written, timeLeft, times, over
    happened = False
    try:
        for i in range(len(written)):
            if(written[i] != true[i]):
                trtl.pencolor("red")
                happened = True
        if not happened:
            trtl.pencolor("lime")
        if written == true:
            count+=1
            try:
                true = bank[count]
                times += (5 - timeLeft)
                timeLeft = 6
            except IndexError:
                over = True
                trtl.clear()
                trtl.write(written, align="center", font=("Arial", 30, "normal"))
                #wn.bgcolor("lime")
                sleep(1)
                aspw = times/len(bank)
                wpm = len(bank)/((round(aspw, 3) * len(bank))/60)
                wn.textinput("Orangutan OS", "You took an average of "+str(round(aspw, 3))+f" seconds to type each word ({round(wpm, 1)} WPM).")
                wn.bye()
            trtl.clear()
            trtl.write(written, align="center", font=("Arial", 30, "normal"))
            sleep(0.1)
            helper.clear()
            helper.write(true, align="center", font=("Arial", 30, "normal"))
            written = ""
    except IndexError:
        trtl.pencolor("red")
   

def char(char:str):
    global written,inputted
    inputted = True
    written += char
    check()
    trtl.clear()
    trtl.write(written, align="center", font=("Arial", 30, "normal"))

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

def space():char(' ')

def backspace():
    global written
    nwritten = ""
   
    for i in range(len(written) - 1):
        nwritten += written[i]
    trtl.clear()
    written = nwritten
    check()
    trtl.write(written, align="center", font=("Arial", 30, "normal"))

wn.listen()
wn.ontimer(countdown, 1000)

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

wn.mainloop()
