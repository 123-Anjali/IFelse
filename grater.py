# a=55
# b=100
# if a<b:
#     print("b is grater than a")  
# elif b>a:
#     print("b is grater  than a")
# else:
#     print("nothing")


a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print("a is grater")
elif b>a and b>c:
    print("b is grater")
elif c>a and c>b:
    print("c is grater")
else:
    print("invailid")
