pin=7645
mainbalance=20000
inputpin=int(input("Enter pin Number:"))
if inputpin==pin:
    print("1.Withdraw\n 2.Balance check\n 3.Deposit \n 4.Exit\n")
    print("Select option which you want to perform")
    choose=int(input())
    if choose==1:
        print("Enter amount you want to withdraw")
        withdraw=int(input())
        if withdraw<=mainbalance and withdraw>0:
            print("Take your cash")
            mainbalance=mainbalance-withdraw
            print("After withdraw , mainbalance")
            print(mainbalance)
        else:
            print("insufficient amount,")

    elif choose==2:
        print("2")

    elif choose==3:
        print("3")

    elif choose==4:
        print("4")

    else:
        print("Invalid option")
    


else:
    print("Invalid pin number")
