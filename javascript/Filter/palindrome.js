const data=[{ name: 'sun'},
{ name: 'malayalam'},
{ name: 'bob'},
{ name: 'David'},
{ name: 'noon'},
{ name: 'words'}];
const y=data.filter(e=>e.name==e.name.split('').reverse().join(''))
console.log(y)



