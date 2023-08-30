st=int(input())
end=int(input())
s=0
for i in range(st,end+1):
    if(i%9==0):
        print(i,end=" ")
        s=s+i
print("\n",s)