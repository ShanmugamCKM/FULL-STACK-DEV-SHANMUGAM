function hobby(inputArray, hobbyToFilter) {
    return inputArray.filter(e => e.hobbies.includes(hobbyToFilter));
  }
const ph = [
    { name: 'Alice', hobbies: ['Reading', 'Painting', 'Hiking'] },
    { name: 'Bob', hobbies: ['Gaming', 'Cooking', 'Photography'] },
    { name: 'Charlie', hobbies: ['Singing', 'Dancing', 'Swimming'] },
    { name: 'David', hobbies: ['Traveling', 'Coding', 'Biking'] },
    { name: 'Eve', hobbies: ['Writing', 'Yoga', 'Gardening'] },
    { name: 'Frank', hobbies: ['Sports', 'Music', 'Cooking'] },
    { name: 'Grace', hobbies: ['Drawing', 'Reading', 'Hiking'] },
    { name: 'Hank', hobbies: ['Photography', 'Skiing', 'Camping'] },
    { name: 'Ivy', hobbies: ['Painting', 'Dancing', 'Traveling'] },
    { name: 'Jack', hobbies: ['Gaming', 'Hiking', 'Cooking'] }
  ];
const h='Gaming';
const print = hobby(ph, h);
console.log(print);
  