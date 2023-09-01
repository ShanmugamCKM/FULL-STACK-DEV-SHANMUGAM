def min(a):
    min=a[0]
    for i in range(len(a)):
        if(min>a[i]):
            min=a[i]
    return(min)
a = [12, 65, 54, 39, 102, 37, 0, 15]
s=min(a)
print(s)