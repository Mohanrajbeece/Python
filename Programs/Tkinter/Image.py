"""from tkinter import *
from tkinter import ttk

root = Tk()
label = Label(root, text="This is Image").pack(side=TOP, pady=10)

path = PhotoImage(file="Image.jpg")
label_image = Label(root, image=path,width=400, height=400)
label_image.pack()

root.geometry("600x440")
root.title("Python")
root.mainloop()"""

from tkinter import *
from tkinter import ttk

root = Tk()
label = Label(root, text="This is Image").pack(side=TOP, pady=10)

path = PhotoImage(file="D:\Python\Advance\Image.jpg")
label_image = Label(root, image=path,width=400, height=400)
label_image.pack()

root.geometry("600x440")
root.title("PythonLobby.com")
root.mainloop()
