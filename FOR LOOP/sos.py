n=int(input())
x=3
s=1
v=0
for i in range(1,n+1):
    s=s*i
    print(s)
    t=x**i
    print(t)
    u=t/s
    print(u)
    v=v+u
    print(v)
print(v+1)