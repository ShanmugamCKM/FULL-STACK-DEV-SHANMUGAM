def remove(s):
    c=[]
    for i in s:
        if i not in c:
            c.append(i)
    print(c)
n=[1,3,5,7,7,9,9]
remove(n)