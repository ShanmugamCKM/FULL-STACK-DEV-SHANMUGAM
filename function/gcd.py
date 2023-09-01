def gcd_d(a,b):
    gcd=1
    for i in range(1,(min(a,b))+1):
        print(i)
        if(a%i==0 and b%i==0):
            gcd=i
            print(gcd)
    return gcd
n=int(input("enter the first number : "))
m=int(input("enter the second number : "))
gcd=gcd_d(n,m)
print("Gcd of",n,"and",m,"is",gcd)      







        