from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Mohan")
root.geometry("300x200")
def submit():
    print("Hello Kavin")
r=Button(root,text="Kavinezhilan",activebackground="Blue",activeforeground="red",command=submit)
r.pack()
a=Label(root,text="Mohan", font=("Ariel",15),fg="blue",bg="red")
a.pack()
lbl=Label(root,text="Kavin", font=("Times new roman",25),fg="orange",bg="yellow")
lbl.pack()
m=Button(root,text="Mohan", font=("Ariel",15),fg="blue",bg="red")
m.pack()
def click():
    messagebox.showinfo("Information","Hello Kavin")
k=Button(root,text="Kavinezhilan",command=click,activebackground="Blue",activeforeground="red",pady=20)
k.pack(side=RIGHT)
root.mainloop()
