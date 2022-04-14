num=int(input("enter the number"))
if num>=1 and num<10:
    aim=input("what is your aim")
    if aim>"a"or aim>"A" and aim<"z" or aim<"Z":
        print(aim)
if num==10:
    sub=input("enter the sub")
    if sub>"a" or sub>"A" and sub<"z" or sub<"Z":
        print(sub)
if num==11 or num==12:
    college=input("enter the college")
    if college>"a"or college>"A" and college<"z" or college<"Z":
        print(college)
        course=input("enter the college")
        if course>"a" or course>"A"  and course<"z" or course<"Z":
            print(course)
    