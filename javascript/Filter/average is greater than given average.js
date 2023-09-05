const students = [
    {
      name: 'Student 1',
      grades: {
        math: 85,
        science: 78,
        history: 92,
        english: 88,
        art: 76,
      },
      average:84
    },
    {
      name: 'Student 2',
      grades: {
        math: 90,
        science: 82,
        history: 75,
        english: 89,
        art: 93,
      },
      average:86
    },
    {
      name: 'Student 3',
      grades: {
        math: 77,
        science: 68,
        history: 91,
        english: 59,
        art: 85,
      },
      average:76
    },
    {
      name: 'Student 4',
      grades: {
        math: 65,
        science: 79,
        history: 57,
        english: 91,
        art: 48,
      },
      average:68
    },
    {
      name: 'Student 5',
      grades: {
        math: 82,
        science: 76,
        history: 50,
        english: 87,
        art: 84,
      },
      average:75
    },
    {
        name: 'Student 6',
        grades: {
          math: 93,
          science: 96,
          history: 90,
          english: 97,
          art: 100,
        },
        average:95
      },

];
const a=students.filter(e=>e.average>80)
console.log(a);
  