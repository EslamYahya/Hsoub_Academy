function Page(index) {
    this.index= index;
}

function Book() {
    this.pages = [];
    console.log("book consist of pages");

    this.add_page = function (index) {
        this.pages.push(Page(index));
        console.log('add to book page' + index);
    }
}
  
let book = new Book();
book.add_page(1);
book.add_page(2);
