n=int(input("enter the year : "))
if(n%400==0 or (n%4==0 and n%100!=0)):
    print(n,"is a leap year")
elif(n%4==1):
    print("3 year")
elif(n%4==2):
    print("2 year")
elif(n%4==3):
    print("1 year")

