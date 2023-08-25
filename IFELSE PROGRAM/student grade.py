sub1=int(input("tamil"))
sub2=int(input("English"))
sub3=int(input("maths"))
sub4=int(input("science"))
sub5=int(input("social"))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")