def Area_Rectangle(l,b,h):
    v=l*b*h
    return v
    
user_input1=int(input("enter the length : "))
user_input2=int(input("enter the breath : "))
user_input3=int(input("enter the height : "))
v=Area_Rectangle(user_input1,user_input2,user_input3)
print(v)