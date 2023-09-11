c=[
    {vegetables:"carrot",  quantity:1,price:30},
    {vegetables:"beetroot",quantity:2,price:40},
    {vegetables:"banana",  quantity:3,price:20},
    {vegetables:"orange",  quantity:4,price:10},
    {vegetables:"apple",   quantity:5,price:100}
]
d=c.reduce((a,b)=> a+(b.price*b.quantity),0)
console.log(d)