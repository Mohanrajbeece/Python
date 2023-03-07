#Example1
"""from tkinter import *

#creating root window
root = Tk()

year= IntVar()
#creating spinbox
sbox = Spinbox(root, from_ = 1990, to = 2018, textvariable = year)
sbox.pack(pady=20)

root.geometry('350x250')
root.title("PythonLobby")
root.mainloop()"""


#Example2

from tkinter import *

#creating root window
root = Tk()

year= IntVar()
#creating spinbox
sbox = Spinbox(root, from_ = 1990, to = 2018, textvariable = year, state="readonly")
sbox.pack(pady=20)

root.geometry('350x250')
root.title("PythonLobby")
root.mainloop()
