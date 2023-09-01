def common_elements(a,b):
    c=[]
    for i in a:
        for j in b:
            if(i==j):
                c.append(i)
    return c
a=[1,2,3,4,5]
b=[2,5,3,8,9]
c=common_elements(a,b)
print(c)
