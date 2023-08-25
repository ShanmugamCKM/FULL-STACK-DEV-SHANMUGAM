age=int(input())
income=int(input())
if((age<18) or (age>65)):
    print("No Retirement savings needed") 
elif (income <= 6,00,000):
    print("Low retirement Savings goal")
elif (income>=600001) and (income<=900000):
    print("Middle retirement savings goal")
else:
    print("High retriement savings goals")