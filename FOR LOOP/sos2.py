n=int(input())
w=0
for i in range(1,n+1):
    s=i*i
    w=w+s
    print(i,end="*")
    print(i,end="=")
    print(s)
print("\n",w)