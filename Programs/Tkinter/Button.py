#Example:
"""from tkinter import *
top=Tk()
top.geometry("200x100")
b=Button(top,text="Simple")
b.pack()
top.geometry('250x200')
top.mainloop()"""


#Example2
"""from tkinter import *

# creating root window
root = Tk()
root.title("Welcome to Python Lobby")
# function defined which is called when button is clicked
def clicked():
    print("I am clicked")
# placing Button to our GUI app
btn = Button(root, text="Click me", command = clicked)
btn.pack()
root.geometry('250x200')
root.mainloop()"""


#Example3:
from tkinter import *
from tkinter import messagebox  
  
top = Tk()  
  
top.geometry("200x100")  
  
def fun():  
    messagebox.showerror("Information","information")  
  
  
b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=30)  
  
b2 =Button(top, text = "Blue",activeforeground = "blue",activebackground = "pink",pady=10)  
  
b3 = Button(top, text = "Green",command = fun,activeforeground = "green",activebackground = "pink",pady = 10)  
  
b4 = Button(top, text = "Yellow",activeforeground = "yellow",activebackground = "pink",pady = 10)  
  
b1.pack(side = LEFT)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)  
  
top.mainloop()  
