c=[
    {name:"kavin",  age:21},
    {name:"kumar",age:23},
    {name:"sanjai",  age:25},
    {name:"thanishka",  age:27},
    {name:"sajana",   age:29}
]
d=c.reduce((a,b)=>a+b.age,0)
console.log(d/5)