n=int(input("enter the number : "))
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
while(n!=0):
    s=n%10
    if(s==1):
        a=a+1
    elif(s==2):
        b=b+1
    elif(s==3):
        c=c+1        
    elif(s==4):
        d=d+1
    elif(s==5):
        e=e+1
    elif(s==6):
        f=f+1
    elif(s==7):
        g=g+1
    elif(s==8):
        h=h+1
    elif(s==9):
        i=i+1
    elif(s==0):
        j=j+1                
    n=n//10
print("the frequency of 1 is",a)
print("the frequency of 2 is",b)
print("the frequency of 3 is",c)
print("the frequency of 4 is",d)
print("the frequency of 5 is",e)
print("the frequency of 6 is",f)
print("the frequency of 7 is",g)
print("the frequency of 8 is",h)
print("the frequency of 9 is",i)
print("the frequency of 0 is",j)