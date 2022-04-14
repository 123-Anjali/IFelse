# n=int(input("enter the number"))
# if n>0:
#     print(n,"*",1,"=",n*1)
#     print(n,"*",2,"=",n*2)
#     print(n,"*",3,"=",n*3)
#     print(n,"*",4,"=",n*4)
#     print(n,"*",5,"=",n*5)
#     print(n,"*",6,"=",n*6)
#     print(n,"*",7,"=",n*7)
#     print(n,"*",8,"=",n*8)
#     print(n,"*",9,"=",n*9)
#     print(n,"*",10,"=",n*10)


n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    while j<10:
        print(i,"*",j,"=",j*i)
        print()
        j=j+1
    i=i+1

