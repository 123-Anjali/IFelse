num=int(input("enter the number"))
f=num//1%10
sec=num//10%10
third=num//100%10
four=num//1000%10
five=num//10000%10
revrse=(f*10000)+(sec*1000)+(third*100)+(four*10)+(five*1)
print(revrse)