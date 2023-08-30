n=int(input("enter the number : "))
m=1
while(n!=0):
    s=n%10
    print(s)
    m=m*s
    print(m)
    n=n//10
    print(n)
print(m)