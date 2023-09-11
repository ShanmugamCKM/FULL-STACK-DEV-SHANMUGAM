c=[
    {vegetables:"carrot",price:30},
    {vegetables:"beetroot",price:40},
    {vegetables:"banana",price:20},
    {vegetables:"orange",price:10},
    {vegetables:"apple",price:100}
]
d=c.reduce((a,b)=> a+b.price,0)
console.log(d);