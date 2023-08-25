s=int(input())
d=int(input())
if(s<120 and d<80):
    print("normal")
elif(s>=120 and s<=129) and (d<80):
    print("elevated")
elif(s>=130 and s<=139) and (d>=80 and d<=89):
    print("stage 1 hypertension")
elif(s>=140 and d>=90):
    print("stage 2 hypertension")