cs=int(input())
if(cs<600):
    print("poor credit")
elif(cs>=600 and cs<=699):
    print("fair credit")
elif(cs>=700 and cs<=799):
    print("good credit")
else:
    print("excellent")