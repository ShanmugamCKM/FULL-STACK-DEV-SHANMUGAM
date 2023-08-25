input=int(input())
if ((input >= 65 and input <= 90) or (input >= 97 and input <= 122)):
     print(" Alphabet ")
elif (input >= 48 and input <= 57):
    print(" Digit ")
else:
    print(" Special Character ")