even=int(input())
s=0
for i in range(2,(even*2)+1,2):
    if(i%2==0):
        print(i,end=" ")
        s=s+i
print("\nsum",s)