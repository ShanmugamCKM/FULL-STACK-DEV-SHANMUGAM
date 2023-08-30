num=int(input())
s=num-1
a=1
for i in range(1,num+1):
    for j in range(0,s):
        print(end=" ")
    s=s-1    
    for j in range(1,i+1):
        print(a,end=" ")
        a=a+1
    print()