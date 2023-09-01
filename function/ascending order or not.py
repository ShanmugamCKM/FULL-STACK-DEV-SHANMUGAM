def asc(s):
    flag = 0
    i = 1
    while i < len(s):
	    if(s[i] < s[i - 1]):
		    flag = 1
	    i=i+1
    if (not flag) :
	    print ("Yes,sorted.")
    else :
	    print ("No,not sorted.")
t= [1, 13,4, 5, 8, 10]
n=asc(t)
