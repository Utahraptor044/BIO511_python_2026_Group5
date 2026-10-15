import math

class MyClass:
    def __init__(self, type): #Weapons can be an object, an obstacle, an opponent... 
        self.type = type

coe33 = MyClass("RPG")
botw = MyClass("Action Adventure")
homeworld = MyClass("RTS")

print(coe33)
print(coe33.type)

#########################################################################
### book management ###

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrowed = None

    def __str__(self):
        # The __str__ dunder method will be called when using print(book_obj)        
        return f"Informative message about the book. You can also use attributes {self.title}"

# Create a book of available in the library
class Library:
    def __init__(self, book):
        self.book = []
        storage = {}

    def add_book(self, book):
        self.book.append(self.book)
        storage[self.book] = "available"

    def borrowed(self, name):
        storage.update({self.book : name})

    def return_book(self, book, name):
        storage.update({book: "available"})




class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = []



book1 = Book("The lord of the ring, The Fellowship of the Ring", "J. R. R. Tolkien", "1954")
book2 = Book("L'étranger", "Albert Camus", "1942")
book3 = Book("The capital", "Karl Markx", "1867")
book4 = Book("Les schtroupfs noirs", "Peyo", "1963")
book5 = Book("Eragon", "Christopher Paolini", "1983")
book6 = Book("Berserk: tome 1", "Kentaro Myura", "1990")
book7 = Book("1984", "George Orwell", "1949")

library = Library(book7)
library.add_book(book1)


print(book1.title)

#############################################################################################

class Parrot:
    def speak(self, text):
        print(f"Parrot says \"{text}\"")

my_parrot = Parrot()
my_parrot.speak("G'd day!")



################################################################################################

### Working with methods ###
        
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        add = self.num1 + self.num2
        return add

    def sub(self):
        sub = self.num1 - self.num2
        return sub

    def mult(self):
        mult = self.num1 * self.num2
        return mult


attempt1 = Calculator(3, 4)
print(attempt1.mult())


### Calculate the properties of a circle
###   ###   ###
# perimeter = 2*pi*rayon
# area = rayon**2 * pi

class Circle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        perimeter = 2 * self.rayon *math.pi
        return perimeter

    def calc_area(self):
        area = self.rayon**2 *math.pi
        return area

circ1 = Circle(float(input("Enter a radius: ")))
print(circ1.calc_perimeter())
print(circ1.calc_area())

print(type(circ1))


##################################################################################
