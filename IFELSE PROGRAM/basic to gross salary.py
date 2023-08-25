ba = float(input("Enter your basic salary: "))
if ba <= 10000:
    hra = (20/100)*ba
    da = (80/100)*ba
    print(ba + hra + da, "is your gross salary.")
elif ba <= 20000:
   hra = (25/100)*ba
   da = (90/100)*ba
   print(ba + hra + da, "is your gross salary.")
elif ba > 20000:
   hra = (30/100)*ba
   da = (95/100)*ba
   print(ba + hra + da, "is your gross salary.")