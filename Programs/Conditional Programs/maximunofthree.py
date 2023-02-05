number1=int(input("Enter the input number1:"))
number2=int(input("Enter the input number2:"))
number3=int(input("Enter the input number3:"))
if(number1>number2) and (number1>number3):
    print("Number1 is the biggest:",number1)
elif(number2>number1) and (number2>number3):
    print("Number2 is the biggest:",number2)
else:
    print("Number3 is the biggest:",number3)