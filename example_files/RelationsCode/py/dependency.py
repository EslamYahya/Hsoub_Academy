class Person:
    def __init__(self):
        pass

    def has_read(self, book):
        print('person uses the book')
        return True

class Book:
    def __init__(self):
        pass
    # code here

book = Book()
person = Person()
print(person.has_read(book))
