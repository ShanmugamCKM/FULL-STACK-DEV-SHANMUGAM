star=int(input())
s=star-1
for i in range(1,star+1):
    for j in range(0,s):
        print(end=" ")
    s=s-1    
    for j in range(1,i+1):
        print("*",end=" ")
    print()
a=" "
for i in range(1,star+1):
    for j in range(0,s):
        print(end=" ")
    s=s-1    
    for j in range(1,i+1):
        a="*"+a
    print(a)