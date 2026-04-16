# Python project with Tkinter
# general lightweight training programme
# Attempt 1
# File: pythonProject1.py
# 2026

# Section I: Functions
def advance():
    print(currentScreen)
    nextScreen = currentScreen+1
    nextScreen.pack()
    currentScreen.destroy()
    currentScreen = nextScreen

# Section II: Imports
from tkinter import *
from os import getlogin

# Section III: Initialisation 1
root = Tk()

# Section IV: Screens
_000 = Frame(root, width=640, height=480)
_001 = Frame(root)

screens = [
    _000,
    _001
]

# Section III: Initialisation 2
_000.pack()
currentScreen = 000

# Section V: Widgets
w000 = Label(_000, text="Welcome, " + getlogin(), font="Times 40 bold")
w000.place(relx=0.5, rely=0.5, anchor="center")

w001 = Button(_000, text="QUIT", fg="red", bg="black", command=root.destroy)
w001.place(relx=0.4, rely=0.6, anchor=CENTER)

w002 = Button(_000, text="advance", command=advance)
w002.place(relx=0.6, rely=0.6, anchor=CENTER)

# Section III: Initialisation 3
root.mainloop()