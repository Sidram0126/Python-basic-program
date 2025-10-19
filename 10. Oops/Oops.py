# 1 Create a class Car with attributes brand, model, and year. Create an object and print its details.
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def show_details(self):
            print("Car Details:")
            print("Brand:",self.brand)
            print("Model:",self.model)
            print("Year:",self.year)
car1=Car("Toyota","Camry",2020)            
car1.show_details()
print("-----------------------------------")


# 2 Add a method start() that prints 'Car is starting…'
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_details(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        
    def start_car(self):
        self.start = "Car is starting......"
        return self.start
    
car1 = Car("Toyota", "Camry", 2020)            
car1.show_details()    
print(car1.start_car())
print("-------------------------------------")


# 3 Create a Student class with a method to calculate average marks.

class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

    def calculate_total(self):
        return self.phy + self.chem + self.maths

    def calculate_average(self):
        return self.calculate_total() / 3

student1 = Student(85, 90, 78)
print("Total Marks:", student1.calculate_total())
print("Average Marks:", student1.calculate_average())
print("-----------------------------------")


# 4 Demonstrate the concept of constructor (__init__) in a class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
person1 = Person("Sid", 26)
person1.display_info()
print("-----------------------------------")


# 5 Create a BankAccount class with deposit() and withdraw() methods.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrew:", amount)

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
account1 = BankAccount("123456789",10000)
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()
print("---------------------------------")


# 6 Implement inheritance: Animal → Dog and Cat, each overriding speak().
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
dog1 = Dog()
cat1 = Cat()
print("Dog says:", dog1.speak())
print("Cat says:", cat1.speak())
print("---------------------------------")


# 7 Demonstrate encapsulation by using private variables (__balance).
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print("Withdrew:", amount)

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance)
account1 = BankAccount("987654321", 5000)
account1.deposit(1000)
account1.withdraw(2000)
account1.display_balance()
print("---------------------------")


# 8 Demonstrate polymorphism using a common method with different implementations.
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print("Area:", shape.area())
print("-----------------------------")


# 9 Create a Student Management System using OOP (add, update, and display students).
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

students = []
def add_student(name, age):
    student = Student(name, age)
    students.append(student)

def display_students():
    for student in students:
        student.display_info()
      
add_student("Sid", 26)
add_student("Ram", 25)
display_students()
print("-----------------------------")


# 10 Create a Library System with classes for Book, Member, and Library.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def display_info(self):
        print("Name:", self.name)
        print("Member ID:", self.member_id)

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        print("Books in Library:")
        for book in self.books:
            book.display_info()
            print("---------------------------------")

    def display_members(self):
        print("Library Members:")
        for member in self.members:
            member.display_info()
            print("---------------------------------")
library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
member1 = Member("Sid", "M001")
member2 = Member("Ram", "M002")
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)
library.display_books()
library.display_members()
print("---------------------------------")