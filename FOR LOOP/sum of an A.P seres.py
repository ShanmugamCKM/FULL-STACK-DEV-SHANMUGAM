st=int(input())
count=int(input())
difference=int(input())
w=0
s=st
for i in range(st,count):
    s=s+difference
    w=w+s
    print(s,end=" ")
print("\n",w+1)