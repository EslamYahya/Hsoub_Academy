class Page:
    def __init__(self, index):
        self.index = index
    
class Book:
    def __init__(self):
        self.pages = []
        
    print("book consist of pages")

    def add_page(self, index):
        self.pages.append(Page(index))
        print("add to book page", index)

book = Book()
book.add_page(1)
book.add_page(2)
