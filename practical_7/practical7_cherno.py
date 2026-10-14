import math

""" class Book:
    def __init__(self,title, author,year):

        self.title1  = title
        self.author = author
        self.year = year

favBook = Book("The Eyes of the Dragon", "Stephen King", 1984)
overdueBook = Book("Chamber of Secrets", "J,K. Rowling", 2001)

print(favBook)
print(favBook.author)

print(overdueBook)
print(overdueBook.author)
print(overdueBook.title1)

class Calculator:
    def __init__(self,number1,number2):
        self.n1=number1
        self.n2=number2

    def sum(self):
        sum = self.n1 + self.n2
        return sum

    def divide(self):
        divide = self.n1/self.n2
        return divide
    
    def multiply(self):
        multiply = self.n1*self.n2
        return multiply
    def subtract(self):
        subtract = self.n1-self.n2
        return subtract


Robot = Calculator(5,6)

print(Robot.sum())
print(Robot.divide())
print(Robot.multiply())
print(Robot.subtract())

class Circle:
    def __init__(self,radius):

        self.radius = radius
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):

        circumference = round(2*math.pi*self.radius,2)
        return circumference
    
    def calc_area(self):
        
        area = round(math.pi*self.radius ** 2,2)
        return area

print("Input the Circle's radius in cm: ")
Circus = Circle(float(input()))


print(f"The area of the circle is {Circus.area} cm²")
print(f"The circumference of the circle is {Circus.perimeter} cm") """

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrower = None

    def __str__(self):
        # The __str__ dunder method will be called when using print(book_obj)
        return f"Informative message about the book. You can also use attributes {self.title}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        book.available = True        
    
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            book.available = False
        else:
            print("Book not found in the library")

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self,library,book,member):
        if book in library.books and book.available:
            book.borrower = member.name
            library.books.remove(book)
            book.available = False
            self.borrowed_books.append(book)

    def return_book(self,book,name):
        if book in self.books and not book.available:
            book.available = True
            book.borrower = None
            name.borrowed_books.remove(book)

# Example usage
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
library = Library()
library.add_book(book1)  # Should add book1 to the library and make it available for borrowing
member1 = Member("Alice")
member1.borrow_book(library,book1,member1)  # Now the book should be borrowed by Alice
print(member1.borrowed_books)
print("Available books:", [str(book) for book in member1.borrowed_books])