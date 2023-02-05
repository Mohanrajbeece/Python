cost=int(input("Enter the input for cost:"))
kmdrive=int(input("Enter the input for kmdrive:"))
if cost<40000:
    if kmdrive<10000:
        print("buy the vehicle")  
    else:
         print("Dont buy")
else:
   print("Too much cost")