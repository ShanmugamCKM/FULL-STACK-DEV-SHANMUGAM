c=[
    {category:"fruits",price:30},
    {category:"fruits",price:40},
    {category:"vegetables",price:20},
    {category:"fruits",price:10},
    {category:"vegetables",price:100}
]
d=c.reduce((a,b)=> {
    if(b.category == "vegetables")
       return a+b.price;
    else
       return a;
},0)
console.log(d);