from random import choice
from time import sleep as wait
import turtle

trtl = turtle.Turtle(visible=False)
wd = turtle.Screen()
wd.bgcolor("black")
wd.title("Orangutan OS - [wordle.exe]")
wd.setup(width=500,height=650)
trtl.pu()
words = ['Apple',
    'Beach', 
    'Brain', 
    'Bread', 
    'Brush', 
    'Chair', 
    'Chest', 
    'Chord', 
    'Click', 
    'Clock',
    'Cloud', 
    'Dance', 
    'Diary', 
    'Drink', 
    'Earth', 
    'Flute', 
    'Fruit', 
    'Ghost', 
    'Grape',
    'Green', 
    'Happy', 
    'Heart', 
    'House', 
    'Juice', 
    'Light', 
    'Money', 
    'Music', 
    'Party',
    'Pizza', 
    'Plant', 
    'Radio',
    'River', 
    'Salad', 
    'Sheep', 
    'Shoes', 
    'Smile', 
    'Snack',
    'Snake', 
    'Spice', 
    'Spoon', 
    'Storm', 
    'Table', 
    'Toast', 
    'Tiger', 
    'Train', 
    'Water',
    'Whale', 
    'Wheel', 
    'Woman', 
    'World', 
    'Write', 
    'Youth', 
    'Abyss', 
    'Ample', 
    'Ankle',
    'Aroma', 
    'Aural', 
    'Began', 
    'Blunt', 
    'Braid', 
    'Brisk', 
    'Bumpy', 
    'Chive', 
    'Clasp',
    'Crave', 
    'Crest', 
    'Dusky', 
    'Dwell', 
    'Elite', 
    'Ember', 
    'Evade', 
    'Evoke', 
    'Fable',
    'Flair', 
    'Fluke', 
    'Folly', 
    'Giddy', 
    'Gloom', 
    'Gorge', 
    'Gusty', 
    'Haste', 
    'Hunch',
    'Ivory', 
    'Jaded', 
    'Jazzy', 
    'Jolly', 
    'Joust', 
    'Jumpy', 
    'Knack', 
    'Knave', 
    'Knead',
    'Kudos', 
    'Lanky', 
    'Latch', 
    'Lolly', 
    'Lurid', 
    'Mirth', 
    'Moody', 
    'Mourn', 
    'Mower',
    'Muggy', 
    'Nanny', 
    'Nappy', 
    'Nerve', 
    'Nifty', 
    'Nudge', 
    'Olive', 
    'Ounce', 
    'Ovals',
    'Peppy', 
    'Pique', 
    'Plush', 
    'Poise', 
    'Quail', 
    'Quake', 
    'Quell', 
    'Quill', 
    'Quirk',
    'Spicy', 
    'Stilt', 
    'Swirl', 
    'Toast', 
    'Tonic', 
    'Tweak'
]
word = choice(words).upper()

attempts = 1
game_status = 'ongoing'

# Popup-based input keeps the original simple Wordle flow without requiring a terminal.
while game_status == 'ongoing' and attempts <= 6:
    guess = wd.textinput("Orangutan OS - Wordle", "Insert five letter word:")

    if guess is None:
        wd.bye()
        break

    guess = guess.upper()

    while len(guess) != 5:
        guess = wd.textinput("Orangutan OS - Wordle", "Word must be exactly five letters long:")
        if guess is None:
            wd.bye()
            break
        guess = guess.upper()

    if not wd._root:
        break

    trtl.goto(-125,(200 - (attempts * 65)))

    if guess != word:
        x = 0

        for i in guess:
            if i in word:
                if word[x] == guess[x]:
                    trtl.color("lime")
                else:
                    trtl.color("yellow")
            else:
                trtl.color("white")
            trtl.write(i, font=("Arial", 80, "bold"), align="center")
            trtl.fd(50)
            x += 1
        attempts += 1
    else:
        trtl.goto(-125,200 - (attempts * 65))
        trtl.color("lime")
        for i in word:
            trtl.write(i, font=("Arial", 74, "bold"), align="center")
            trtl.fd(50)
        wd.textinput("Orangutan OS - Wordle", f"Correct! Answer guessed in {attempts} attempts.")
        game_status = 'over'

if attempts > 6 and game_status == 'ongoing':
    wait(1)
    trtl.color("red")
    wd.textinput("Orangutan OS - Wordle", f"You are out of attempts. The answer was {word}.")

wd.mainloop()
