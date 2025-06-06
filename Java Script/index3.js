let rows = prompt('please enter rows count.');
for (let row = 1; row <= rows; row++){
    let stars = '';
    for (let i = 0; i < row; i++){
        stars += '*';
    }
    console.log(stars);
    
}