b=float(input())
if(b<18.5):
    print("under weight")
elif(b>=18.5 and b<=24.9):
    print("normal weight")
elif(b>=25 and b<=29.9):
    print("over weight")
else:
    print("obese")