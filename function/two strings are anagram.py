
from collections import Counter
def check(str1,str2):
    print(Counter(str1))
    print(Counter(str2))
    if(Counter(str1)==Counter(str2)):
       print("The strings are anagrams")
    else:
        print("The strings are not anagrams")
str1=str(input("string 1:"))
str2=str(input("string 2:"))
check(str1.lower(),str2.lower())
