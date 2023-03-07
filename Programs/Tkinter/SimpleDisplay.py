"""from tkinter import *
  
root=Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for string name and password
name_var=StringVar()
passw_var=StringVar()
 
def submit():
    
    name=int(name_var.get())
    
    password=int(passw_var.get())
    c=name+password
    print(c)
    print(name)
    print(password)
     
name_label = Label(root, text = 'Username', font=('calibre',10, 'bold')).grid(row="0",column="0")

name_entry = Entry(root,textvariable = name_var, font=('calibre',10,'normal')).grid(row="0",column="1")

passw_label = Label(root, text = 'Password', font = ('calibre',10,'bold')).grid(row="1",column="0")
  

passw_entry=Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*').grid(row="1",column="1")

sub_btn=Button(root,text = 'Submit', command = submit).grid(row="2",column="1")

root.mainloop()"""



from tkinter import *
from functools import partial 
root=Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for string name and password
name_var=StringVar()
passw_var=StringVar()
 
def submit(label_result):
 
    name=int(name_var.get())
    password=int(passw_var.get())
    Result=name+password
    label_result.config(text="Result=%d"%Result)
    return
   
    #print("The name is : " , name)
    #print("The password is : " , password)
     
name_label = Label(root, text = 'Username', font=('calibre',10, 'bold')).grid(row="0",column="0")

name_entry = Entry(root,textvariable = name_var, font=('calibre',10,'normal')).grid(row="0",column="1")

passw_label = Label(root, text = 'Password', font = ('calibre',10,'bold')).grid(row="1",column="0")
label_result = Label(root)  
  
label_result.grid(row=7, column=2)  
passw_entry=Entry(root, textvariable = passw_var, font = ('calibre',10,'normal')).grid(row="1",column="1")
submit=partial(submit,label_result)
sub_btn=Button(root,text = 'Submit', command = submit).grid(row="2",column="1")

root.mainloop()
