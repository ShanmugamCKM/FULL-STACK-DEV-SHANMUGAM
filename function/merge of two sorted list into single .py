def sorting(a,b):
    c=[]
    c=a+b
    for i in c:
        for j in range(i+1,len(c)):
            if(i>j):
                temp=j
                i=temp
                print(i)
    return c            
a=[1,2,3,4,5]
b=[6,7,8,9,0]
c=sorting(a,b)
print(c)