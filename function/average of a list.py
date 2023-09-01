def average(s):
    n=0
    for i in s:
        n=n+i
        average=n//len(s)
    print(average)
n=[1,3,5,7,9]
average(n)