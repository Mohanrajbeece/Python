# Importing Tkinter module
"""from tkinter import *

root = Tk()
root.title("PythonLobby")

# Tkinter string variable it can store any string value
value1 = StringVar(root, "3")

rbtn1 = Radiobutton(root, text="Radio Button 1", variable = value1 , value="1")
rbtn1.pack()
rbtn2 = Radiobutton(root, text="Radio Button 2", variable = value1 , value="2")
rbtn2.pack()
rbtn3 = Radiobutton(root, text="Radio Button 3", variable = value1 , value="3")
rbtn3.pack()

root.geometry("250x200")
mainloop()"""





"""from tkinter import *

#root window
root = Tk() 

var = StringVar(root, "1")

# Dictionary to create multiple buttons 
val = {"Radio Button 1" : "1", "Radio Button 2" : "2", "Radio Button 3" : "3", }

# Loop used to create multiple Buttons
for (text, value) in val.items():
	btn = Radiobutton(root, text = text, variable = var, value = value).pack(pady=15)

root.geometry("175x175")
root.title("PythonLobby")
mainloop()"""





from tkinter import *  
  
def selection():  
   selection = "You selected the option " + str(radio.get())  
   label.config(text = selection)  
  
top = Tk()  
top.geometry("300x150")  
radio = IntVar()  
lbl = Label(text = "Favourite programming language:")  
lbl.pack()  
R1 = Radiobutton(top, text="C", variable=radio, value=1,  
                  command=selection)  
R1.pack( anchor = W )  
  
R2 = Radiobutton(top, text="C++", variable=radio, value=2,  
                  command=selection)  
R2.pack( anchor = W )  
  
R3 = Radiobutton(top, text="Java", variable=radio, value=3,  
                  command=selection)  
R3.pack( anchor = W)  
  
label = Label(top)  
label.pack()  
top.mainloop()
