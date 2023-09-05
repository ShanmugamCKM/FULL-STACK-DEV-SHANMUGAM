function filterObjectsByDateRange(inputArray, startDate, endDate) {
    return inputArray.filter(item => {
      const itemDate = new Date(item.date);
      return itemDate >= startDate && itemDate <= endDate;
    });
  }
  const arrayOfObjects = [
    { name: 'Event 1', date: '2023-09-10' },
    { name: 'Event 2', date: '2023-09-15' },
    { name: 'Event 3', date: '2023-09-20' },
    { name: 'Event 4', date: '2023-09-25' },
  ];
  
  const startDate = new Date('2023-09-12');
  const endDate = new Date('2023-09-22');
  
  const filteredArray = filterObjectsByDateRange(arrayOfObjects, startDate, endDate);
  console.log(filteredArray);
  