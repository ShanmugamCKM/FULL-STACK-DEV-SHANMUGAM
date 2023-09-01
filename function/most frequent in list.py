def most_frequent(a):
    count=1
    frequency=0
    for i in a:
        for j in a:
            if(i==j):
                count=count+1
            
        if(count>frequency):
            frequency=count
            num=i
        count=0
    return num,frequency
    
a=[1,7,7,7,2,2,2,2,4,5,6,6]
num=most_frequent(a)
frequency=most_frequent(a)
print(num,frequency)
 

        