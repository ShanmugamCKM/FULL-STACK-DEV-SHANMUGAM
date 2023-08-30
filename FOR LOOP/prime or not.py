p=int(input())
flag=0
for i in range(2,p):
    if(p%i==0):
        flag=1
        break
if(flag==1):
    print("not a prime")
else:
    print("prime")