a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and b>c:
    print("b is second grater")
if b>a and a>c:
    print("a is second grater")
if b>c and c>a:
    print("c is second grater")
else:
    print("invailid")