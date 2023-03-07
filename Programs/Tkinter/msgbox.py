
from tkinter import *
top=Tk()
top.geometry("400x200")
uname=Label(top,text="username").grid(row="0",column="0")
e1=Entry(top,width=20).grid(row="1",column="0")
password=Label(top,text="Password"),Grid(row="1",column="0")
e2=Entry(top,width=20), Grid(row="1",column="1")
top.mainloop()
