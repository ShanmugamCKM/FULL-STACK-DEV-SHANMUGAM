n=int(input("enter the year : "))
if(n%400==0 or (n%4==0 and n%100!=0)):
    print(n,"is a leap year")
elif(n%4==1):
    print(n-1)
elif(n%4==2):
    print(n-2)
elif(n%4==3):
    print(n-3)