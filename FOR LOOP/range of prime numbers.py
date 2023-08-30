st=int(input())
end=int(input())
s=0
for i in range(st,end):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i,end=" ")
            