def avg_even(a):
    s=0
    count=0
    for i in x:
        if(i%2==0):
            s=s+i
            count=count+1
    avg=s/count
    return avg
x=[1,2,3,4,5,6,7,8,9,20]
avg=avg_even(x)
print(avg)
