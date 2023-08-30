odd=int(input())
s=0
for i in range(1,(odd*2)+1):
    if(i%2!=0):
        print(i,end=" ")
        s=s+i
print("\nsum",s)