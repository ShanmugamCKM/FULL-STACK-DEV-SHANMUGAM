n1=int(input())
n2=int(input())
for i in range(2,min(n1,n2)+1):
    if(n1%i==n2%i==0):
        hcf=i
        print(hcf)
        break
lcm=(n1*n2)//hcf
print(lcm)