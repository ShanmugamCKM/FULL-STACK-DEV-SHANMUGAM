h=float(input())
w=float(input())
bmi=float(w/h**2)
if(bmi<18.5):
    print("under weight")
elif(bmi>=18.5 and bmi<=24.9):
    print("normal weight")
elif(bmi>=25 and bmi<=29.9):
    print("over weight")
else:
    print("obese")