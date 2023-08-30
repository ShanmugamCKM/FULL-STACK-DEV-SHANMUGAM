n=int(input())
s=1
t=1
for i in range(2,n+1):
    s=s*10+1
    print(s,end=" ")
    t=t+s
print("\n",t)