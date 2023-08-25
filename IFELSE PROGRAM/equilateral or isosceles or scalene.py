x=int(input())
y=int(input())
z=int(input())
if x == y == z:
    print("Equilateral Triangle")
elif x == y or y == z or z == x:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
 
