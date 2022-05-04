# a=425
# while a< 450:
#     a=a+1
#     k=a-425
#     print(k)





# number=int(input("enter the number"))
# a=[]
# b=[]
# c=[]
# i=0
# while i<number:
#     num=input("enter the name")
#     a.append(num)
#     num1=input("enter the sarname")
#     b.append(num1)
#     num3=int(input("enter the age"))
#     c.append(num3)
#     i=i+1
    # print(a)
# print(b)
# print(c)


# a=[1,2,3,4,5,6,7,8,9]
# num=int(input("enter the number"))
# i=0
# sum=0
# while i<len(a):
#     if a[i]==num:
#         x=i+1
#         while x<len(a):
#             sum=sum+a[x]
#             x=x+1
#     i=i+

# print(sum)


date=int(input("enter the today date"))
month=int(input("enter the current month"))
year=int(input("enter the current year"))
y=str(date)+"/"+str(month)+"/"+str(year)
if date>=1 and date<=31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
    date+=1
    print(str(date)+"/"+str(month)+"/"+str(year))
elif date>=1 and date<=30  and (month==4 or month==6 or month==9 or month==11):
    date+=1
    print(str(date)+"/"+str(month)+"/"+str(year))
elif date==30 or date==31 and (month>=1 and month<=11):
    date+=1
    month+=1
    print(str(date)+"/"+str(month)+"/"+str(year))
elif month==12 and date==31:
    date+=1
    month+=1
    year+=1
    print(str(date)+"/"+str(month)+"/"+str(year))

elif month==2 and date<28:
    date+1
    print(str(date)+"/"+str(month)+"/"+str(year))
elif month==2 and date==28:
    date+=1
    month+=1
    print(str(date)+"/"+str(month)+"/"+str(year))
elif month==2:
    if year%4==0 and date==29:
        date=1
        month+1
        print(str(date)+"/"+str(month)+"/"+str(year))
    elif year%4==0 and date<29:
        date+=1
        print(str(date)+"/"+str(month)+"/"+str(year))
    else:
        ("wrong input")
elif month==12 and date==31:
    date=1
    month=1
    year+=1
    print(str(date)+"/"+str(month)+"/"+str(year))


