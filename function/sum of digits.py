def sod(n):
    m=0
    while(n!=0):
        s=n%10
        m=m+s
        n=n//10
    print(m)
n=int(input())
sod(n)