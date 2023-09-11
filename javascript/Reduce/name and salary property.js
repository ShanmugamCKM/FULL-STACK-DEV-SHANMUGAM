c=[
    {name:"senthil",salary:2000},
    {name:"venkat",salary:20000},
    {name:"paarivendhan",salary:20000000},
    {name:"sriwatson",salary:200000},
    {name:"virus",salary:500000}
]
d=c.reduce((a,b)=> a+b.salary,0)
console.log(d);