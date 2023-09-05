const a = [
    { name: 'John', age: 30 },
    { name: 'Alice', age: 25 },
    { name: 'Bob', age: 40 },
    { name: 'Eva', age: 22 },
    { name: 'Daniel', age: 35 },
    { name: 'Sophia', age: 28 },
    { name: 'Michael', age: 45 },
    { name: 'Olivia', age: 19 },
    { name: 'William', age: 27 },
    { name: 'Emily', age: 33 }
  ];
  const b=a.filter(e=>e.age>25)
  console.log(b)