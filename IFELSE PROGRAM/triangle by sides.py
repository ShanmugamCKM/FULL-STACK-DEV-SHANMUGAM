A=int(input("enter the first side : "))
B=int(input("enter the second side : "))
C=int(input("enter the third side : "))
if((A+B)>C or (B+C)>A or (C+A)>B):
    print("valid")
else:
    print(" not valid")