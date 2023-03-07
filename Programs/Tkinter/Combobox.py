
#With out default value combobox

"""from tkinter import *
from tkinter import ttk as tk

#root window
root = Tk()

#Combobox
fruits = StringVar()
entries = ("Mango", "Apple", "Banana", "Guava",)
box = tk.Combobox(root, value= entries, textvariable = fruits).pack(pady=20)


root.geometry("250x200")
root.title("Python")
mainloop()"""


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

var = tk.StringVar()
fruit = ttk.Combobox(root, width = 27, textvariable = var)

# Adding combobox drop down list
fruit['values'] = (' Guava', ' Mango', ' Apple', ' Banana',)

fruit.pack(pady=20)

# Setting Apple as a default
fruit.current(2)

root.geometry('350x250')
root.title("Python")
root.mainloop()
