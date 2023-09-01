def max(a):
    max=a[0]
    for i in range(len(a)):
        if(max<a[i]):
            max=a[i]
    return(max)
a = [12, 65, 54, 39, 102, 37, 0, 15]
s=max(a)
print(s)