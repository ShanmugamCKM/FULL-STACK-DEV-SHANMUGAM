st=int(input())
item=5
cr=2
s=st
w=0
for i in range(1,item):
    s=s*cr
    print(s)
    w=w+s
print(w+3)