import tkinter as tk
import random

root = tk.Tk()
root.title("Memory Card Flip Game")

# emojis as cards
symbols = ["🍎","🍎","🍌","🍌","🍇","🍇","🍒","🍒"]

random.shuffle(symbols)

buttons = []
first = None
second = None
lock = False

def flip(i):

    global first, second, lock

    if lock:
        return

    buttons[i]["text"] = symbols[i]

    if first is None:
        first = i
    elif second is None and i != first:
        second = i
        check_match()

def check_match():

    global first, second, lock

    if symbols[first] == symbols[second]:

        first = None
        second = None

        check_win()

    else:

        lock = True
        root.after(800, hide_cards)

def hide_cards():

    global first, second, lock

    buttons[first]["text"] = "?"
    buttons[second]["text"] = "?"

    first = None
    second = None
    lock = False

def check_win():

    for b in buttons:
        if b["text"] == "?":
            return

    win = tk.Label(root,text="🎉 You Win!",font=("Arial",20))
    win.grid(row=4,column=0,columnspan=4)

# create grid

for i in range(8):

    btn = tk.Button(root,text="?",font=("Arial",20),
                    width=5,height=2,
                    command=lambda i=i: flip(i))

    btn.grid(row=i//4,column=i%4)

    buttons.append(btn)

root.mainloop()