num = int(input("any number: "))
last_digit = num % 10
first_digit = num
while first_digit >= 10:
    first_digit = first_digit//10
print(first_digit,last_digit)
print(first_digit+last_digit)

