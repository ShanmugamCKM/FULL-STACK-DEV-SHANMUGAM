def convert(a):
    var=""
    for i in a:
        var=var+str(i)
    return int(var)
a=[1,2,3,4]
var=convert(a)
print(var)