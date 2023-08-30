num=int(input())
s=num-1
a=0
m=1
for i in range(1,num+1):
    for j in range(0,s):
        print(end="  ")
    s=s-1    
    for j in range(1,m+1):
            print("*",end=" ")
    m=m+2
    print()
    