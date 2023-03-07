"""#Labels in GUI 
from tkinter import *

# creating root window
root = Tk()

# customizing root window title
root.title("Welcome to Python")
# customizing root window dimension
root.geometry('250x200')

# placing label to our GUI app
name = "We are Python"
lbl = Label(root, text = name, font=("Arial", 12), fg = 'white' , bg='black')
lbl.pack()

root.mainloop()"""

#Example1:
from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  
  
#creating label  
uname = Label(top, text = "Username").grid(row="0",column="0")
  
e1 = Entry(top,width = 20).grid(row="0",column="1")
  
#creating label  
password = Label(top, text = "Password").grid(row="1",column="0")
  
e2 = Entry(top, width = 20, show="*").grid(row="1",column="1")   
sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue").grid(row="2",column="0")
  
  
top.mainloop()  
