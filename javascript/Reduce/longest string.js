c=["kavin","kiruba","mohan","sathish"]
d=c.reduce((a,b)=>a=a.length<b.length ? b:a)
console.log(d);