a=int(input())
b=int(input())
c=int(input())
if(a==b==c or a==b or a==c):
    print(a)
elif(b==c):
        print(b)
elif(a<b and a<c):
        print(a)
elif(b<c):
    print(b)
else:
   print(c)
