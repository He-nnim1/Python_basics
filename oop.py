#oop = object oriented programming

#properties + functions

#class => template

# book title, author, isbn, price
class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def print_details(self):
        print("Title", self.title)
        print("Author", self.author)
        print("Price", self.price)

    def apply_discount(self,discount):
        self.price = self.price * (1 - discount/100)
        print("New Price is", self.price)

b1 = Book("Nuggets of Destiny", "John K. William", "ISB9008", 500)
b2 = Book("Two rivers", "Chinua Achebe", "ISB0442", 250)

b1.print_details()
b1.apply_discount(5)
print(b2.title)


