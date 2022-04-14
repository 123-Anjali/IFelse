a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a==b==c:
    print("equaliteral")
elif a==b or b==c or c==a:
    print("isocles triangle")
elif a!=b!=c:
    print("scalene triangle")
