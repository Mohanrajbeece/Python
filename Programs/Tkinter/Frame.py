from tkinter import *

#root window
root = Tk()
#label
label = Label(root, text ='Python Lobby', font = "60")
label.pack()
#bottom frame
bottom_frame = Label(root,text="", bg="green", width=120, height=100)
bottom_frame.pack(side=LEFT, padx=10)
#top_frame
top_frame = Label(root, text="",bg="red", width=120, height=100)
top_frame.pack(side=RIGHT, padx=10)

root.geometry("300x150")
root.mainloop()
