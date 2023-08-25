age=int(input())
exp=int(input())
if(age<25 and exp<1):
    print("entry level")
elif(age>=25 and age<40) and (exp>=1 and exp <5):
    print("junior")
elif(age>=40) and (exp>=5 and exp<10):
    print("senior")
elif(age>=40 and exp>=10):
    print("expert")
else:
    print("wrong data")
