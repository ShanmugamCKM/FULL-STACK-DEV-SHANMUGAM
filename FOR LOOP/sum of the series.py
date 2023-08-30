n=int(input())
w=0
for i in range(1,n+1):
    s=(10**i)-1
    print(s,end=" ")
    w=w+s
print("\n",w)