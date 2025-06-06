const data = [5, true, "Hello", false, "world", 2 ];

for (let i = 0; i < data.length; i++) {
    if (typeof data[i] === 'string') console.log(data[i]);
}