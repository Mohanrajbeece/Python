"""from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  
  
name = Label(top, text = "Name").place(x = 30,y = 50)  
  
email = Label(top, text = "Email").place(x = 30, y = 90)  
  
password = Label(top, text = "Password").place(x = 30, y = 130)  
  
sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 170)  
  
e1=Entry(top).place(x = 80, y = 50)  
  
  
e2=Entry(top).place(x = 80, y = 90)  
  
  
e3=Entry(top).place(x = 95, y = 130)
print(e1,e2,e3)
  
top.mainloop()  """
from tkinter import *   
from functools import partial
def call_result(label_result,n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)    
    return  
   
root = Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = StringVar()  
number2 = StringVar()  
  
labelNum1 = Label(root, text="A").place(x=30,y=50) 
  
labelNum2 = Label(root, text="B").place(x=30,y=90) 
  
labelResult = Label(root)  
  
labelResult.place(x=30,y=170) 
  
entryNum1 = Entry(root, textvariable=number1).place(x = 80, y = 50)   
  
entryNum2 = Entry(root, textvariable=number2).place(x = 80, y = 90)    
  
call_result = partial(call_result,label_result,number1, number2)  
  
buttonCal = Button(root, text="Calculate", command=call_result).place(x = 95, y = 130)  
  
root.mainloop()  
