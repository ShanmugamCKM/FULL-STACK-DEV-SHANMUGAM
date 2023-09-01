def vowel(ch):
    c=0
    for i in ch:
        if(i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
            c=c+1
    print(c)
s="the world is full of mystery"
vowel(s)