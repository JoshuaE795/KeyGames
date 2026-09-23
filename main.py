import os
import subprocess
import sys
import tkinter as tk

ROOT = os.path.dirname(os.path.abspath(__file__))
GAMES = os.path.join(ROOT, "games")

BG = "#050505"
CARD = "#111111"
CARD_HOVER = "#1c1c1c"
WHITE = "#f5f5f5"
MUTED = "#9b9b9b"
LINE = "#2a2a2a"

GAMES_LIST = [
    ("HANGMAN", "Classic letter guessing", "hangman.py"),
    ("TYPING TEST", "Test your typing speed", "typingtest.py"),
    ("TYPING GAME", "30 words. 5 seconds each.", "typinggame.py"),
    ("WORDLE", "Five-letter word guessing", "wordle.py"),
    ("TIC-TAC-TOE", "Local two-player", "tictactoe.py"),
]


def launch(filename):
    path = os.path.join(GAMES, filename)
    subprocess.Popen([sys.executable, path], cwd=GAMES)


def fade(card, target, steps=8):
    current = card.cget("bg")
    def rgb(value):
        value = value.lstrip("#")
        return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
    a = rgb(current)
    b = rgb(target)
    def step(n=0):
        t = min(n / steps, 1)
        color = "#" + "".join(f"{round(a[i] + (b[i] - a[i]) * t):02x}" for i in range(3))
        card.configure(bg=color)
        for child in card.winfo_children():
            if isinstance(child, tk.Label): child.configure(bg=color)
        if n < steps: card.after(18, step, n + 1)
    step()


root = tk.Tk()
root.title("KEYGAMES")
root.geometry("760x620")
root.minsize(680, 560)
root.configure(bg=BG)

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=46, pady=(38, 12))

title = tk.Label(header, text="KEYGAMES", bg=BG, fg=WHITE, font=("Arial", 28, "bold"))
title.pack(anchor="w")
subtitle = tk.Label(header, text="MINI-GAME COLLECTION", bg=BG, fg=MUTED, font=("Arial", 10, "bold"))
subtitle.pack(anchor="w", pady=(3, 0))

line = tk.Frame(root, bg=LINE, height=1)
line.pack(fill="x", padx=46, pady=(8, 20))

container = tk.Frame(root, bg=BG)
container.pack(fill="both", expand=True, padx=46)

for index, (name, desc, filename) in enumerate(GAMES_LIST):
    card = tk.Frame(container, bg=CARD, height=72, cursor="hand2")
    card.pack(fill="x", pady=6)
    card.pack_propagate(False)

    number = tk.Label(card, text=f"0{index + 1}", bg=CARD, fg="#555555", font=("Arial", 10, "bold"), width=5)
    number.pack(side="left", padx=(18, 0))

    text_frame = tk.Frame(card, bg=CARD)
    text_frame.pack(side="left", fill="both", expand=True, pady=12)
    name_label = tk.Label(text_frame, text=name, bg=CARD, fg=WHITE, font=("Arial", 13, "bold"), anchor="w")
    name_label.pack(anchor="w")
    desc_label = tk.Label(text_frame, text=desc, bg=CARD, fg=MUTED, font=("Arial", 9), anchor="w")
    desc_label.pack(anchor="w", pady=(2, 0))

    arrow = tk.Label(card, text="→", bg=CARD, fg="#666666", font=("Arial", 18))
    arrow.pack(side="right", padx=20)

    widgets = [card, number, text_frame, name_label, desc_label, arrow]
    for widget in widgets:
        widget.bind("<Enter>", lambda e, c=card: fade(c, CARD_HOVER))
        widget.bind("<Leave>", lambda e, c=card: fade(c, CARD))
        widget.bind("<Button-1>", lambda e, f=filename: launch(f))

footer = tk.Label(root, text="SELECT A GAME TO LAUNCH", bg=BG, fg="#555555", font=("Arial", 8, "bold"))
footer.pack(anchor="w", padx=46, pady=(14, 28))

root.mainloop()
