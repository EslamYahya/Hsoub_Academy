function Person() {
    this.hasRead = function (book) {
        console.log('person uses the book');
        return true;
    }
}
  
function Book() {
    //code here
}

let book = new Book();
let person = new Person();
console.log(person.hasRead(book));