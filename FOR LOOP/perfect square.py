st=int(input())
end=int(input())
for i in range(st,end+1):
    s=0
    for j in range(1,i):
        if(i%j==0):
            s=s+j
    if(s==i):
        print(s)