n1=int(input())
n2=int(input())
for i in range(1,min(n1,n2)):
    if(n1%i==0 and n2%i==0):
        gcd=i
print("gcd of 2 numbers",n1,"and",n2,gcd)