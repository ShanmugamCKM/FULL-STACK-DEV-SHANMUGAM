n=int(input())
w=0
for i in range(1,n+1):
    s=1/i**i
    print(s)
    w=w+s
    print(w)
print(float(w))