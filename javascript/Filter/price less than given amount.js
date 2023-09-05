data=[{'price' : 10000},
{'price' : 40000},
{'price' : 90000},
{'price' : 200000},
{'sal' : 75000,'gender' : 'female'}]
a=data.filter(function(e){
    return e.price>40000;
});
console.log(a)
b=data.filter(e=>e.price>40000)
console.log(b)