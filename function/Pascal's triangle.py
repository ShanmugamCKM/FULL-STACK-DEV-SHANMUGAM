def p(n):
    s=n-1
    for i in range(n):
        for j in range(1,s+1):
            print(end=" ")
        s=s-1
        m=1
        for j in range(1,i+1):
            print(' ',m,sep='',end='')
            print(j)
        m=m*(i-j)//j
        print()
n=int(input())
p(n)

"""n=int(input())
s=n-1
for i in range(1,n+1):
    for j in range(0,s):
        print(end=" ")
    s=s-1   
    m=1
    for j in range(1,i+1):
        print(' ',m,sep='',end='')
        print(j)
        #m=m*(i-j)//j
    print()

    """