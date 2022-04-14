print("creat new pasward")
print("strong pasward")
ch=str(input("enter uppar case letter"))
if ch >="A" and ch<="Z":
    ch2=str(input("enter lower case letter"))
    if ch2 >="a" and ch2<="z":
        num=input("enter the number")
        if num>="1" and num<="9":
            sc=input("enter spical character")
            if sc=="@" or sc=="#" or sc=="&" :
                a=(ch+ch2+num+sc)
                print(a)
                if len(a)>=8 or len(a)<=16:
                    print("write pasward")
                else:
                    print("envailid")
            else:
                print("envailid")
        else:
            print("invailid")
    else:
        print("invailid")
else:
    print("invaild")