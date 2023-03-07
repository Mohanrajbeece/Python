from tkinter import *

# creating root window
root = Tk()
root.title("Welcome to Python Lobby")

# placing Entry widget to our GUI app
entry = Entry(root, bg="yellow", fg="red", bd=5)
entry.pack()

root.geometry('250x200')
root.mainloop()
