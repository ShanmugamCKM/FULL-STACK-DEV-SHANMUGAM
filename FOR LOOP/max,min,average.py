a=[1,3,9,5,7]
max=a[0]
min=a[0]
for i in range(len(a)):
    if(max< a[i]):
        max=a[i]
    elif(min>a[i]):
        min=a[i]
print(max)
print(min)
print(len(a))
s=0
for j in a:
    s=s+j
    average=s//(len(a))
print(average)