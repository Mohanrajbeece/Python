"""from tkinter import *
from tkinter import filedialog
#setting up parent window
root = Tk()

#function definition for opening file dialog
def openf():
    file = filedialog.askopenfilename(initialdir='/', title="select file")

file_open = Button(root, text="Open file", command= openf)
file_open.pack(pady=20)

root.geometry("350x200")
root.title("PythonLobby.com")
root.mainloop()"""


#Save File 
from tkinter import *
from tkinter import filedialog
#setting up parent window
root = Tk()

#function definition for opening file dialog
def savef():
    myFile = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if myFile is None:
        return
    data = teditor.get(1.0,'end')
    myFile.write(data)
    myFile.close()

#creating text editor
teditor = Text(root, width=40, height=8)
teditor.pack(pady=10)

file_save = Button(root, text="Save file", command= savef)
file_save.pack(side=LEFT,padx=150)

root.geometry("350x200")
root.title("PythonLobby.com")
root.mainloop()
