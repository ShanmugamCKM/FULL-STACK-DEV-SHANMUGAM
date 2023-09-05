function ne(inputArray, domain) {
    return inputArray.filter(item => {
      return item.email.includes(domain);
    });
  }
const data = [
    { name: 'John Doe', email: 'john.doe@example.com' },
    { name: 'Jane Smith', email: 'jane.smith@example.com' },
    { name: 'Bob Johnson', email: 'bob.johnson@example.in' },
    { name: 'Alice Brown', email: 'alice.brown@example.com' },
    { name: 'Benjamin Taylor', email: 'benjamin.taylor@example.in' },
  ];
v='.com'
const a = ne(data, v);
console.log(a);
  