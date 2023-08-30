n=int(input())
s=n-1
for i in range(1,n+1):
    for j in range(0,s):
        print(end=" ")
    s=s-1    
    for j in range(1,i+1):
        print(i,end=" ")
    print()