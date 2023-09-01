def multiples(n):
    s=1
    s1=1
    for i in range(1,n+1):
        s=1*i
        s1=s1*s
    return s1
n=int(input("enter the number"))
s1=multiples(n)
print(s1)
    