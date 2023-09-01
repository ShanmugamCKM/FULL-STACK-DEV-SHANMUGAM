import math
def heron_triangle(a,b,c):
    s=(a+b+c)/2
    print(s)
    area=math.sqrt(s(s-a)(s-b)(s-c))
    print(area)
    return area
a=float(input("enter the number : "))
b=float(input("enter the number : "))
c=float(input("enter the number : "))
area=heron_triangle(a,b,c)
print(area)