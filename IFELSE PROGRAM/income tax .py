tax=int(input())
if(tax<=300000):
    print("no tax")
elif(tax>=300001 and tax<=600000):
    print("low tax bracket")
elif(tax>=600001 and tax<=900000):
    print("middle tax bracket")
elif(tax>=900001 and tax<=1200000):
    print("high tax bracket")
