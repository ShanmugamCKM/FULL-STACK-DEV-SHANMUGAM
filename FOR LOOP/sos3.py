n=int(input())
w=0
s=0
for i in range(1,n+1):
    s=s+i
    print(s,end=" ")
    w=w+s
print("\n",w)