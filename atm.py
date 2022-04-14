print("welcome to indian bank")
print("swaip your chard")
print(" select language:english,hindi")
lan=input("enter the language")
amount=10000
if lan=="english":
    pin=(input("enter the pin"))
    if pin=="1234":
        print("1,withdrwal")
        print("2,cash enqari")
        print("3,cash transfer")
        choise=(input("enter the choise"))
        if choise=="1":
            withdrwal=int(input("enter the amount"))
            if withdrwal<amount and  withdrwal%100==0:
                print("you can take cash")
            else:
                print("invailid cash amount")
        elif choise=="2":
            print("your balance is",amount)
        elif choise=="3":
            acountnumber=input("enter the acountnumber")
            if acountnumber>="1" and acountnumber<="9":
                    cashtransfer=int(input("enter your amount"))
                    if amount>=cashtransfer:
                        print("cash transfer sucessfuly")
                    else:
                        print("envailid amount")
            else:
                    print("envailid acountnumber")    
        else:
            print("invailid choise")
    else:
        print("envailid pin number")
else:
    print("envailid language")
        


