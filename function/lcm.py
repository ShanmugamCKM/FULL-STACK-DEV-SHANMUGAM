def lcm_a(n,m):
    for i in range(max(n,m),(n*m)+1):
        if (i%n==0 and i%m==0):
            lcm=i
            break
    return lcm

n=int(input("Enter the first number : "))
m=int(input("Enter the second number : "))
lcm=lcm_a(n,m)
print("lcm of",n,"and",m,"is",lcm)    