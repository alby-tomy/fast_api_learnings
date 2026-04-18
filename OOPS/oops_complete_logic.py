from abc import ABC, abstractmethod
import math
from datetime import datetime

"""
COMPREHENSIVE GUIDE TO OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON
====================================================================
This file covers all OOP concepts with practical examples.
"""

# ============================================================================
# 1. CLASSES AND OBJECTS
# ============================================================================

class Dog:
    """Basic class definition"""
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name, age):
        """Constructor - Initialize instance variables"""
        self.name = name
        self.age = age
    
    def bark(self):
        """Instance method"""
        return f"{self.name} says Woof!"
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Class method - works with class not instance"""
        age = 2024 - birth_year
        return cls(name, age)
    
    @staticmethod
    def info():
        """Static method - doesn't need self or cls"""
        return "Dogs are loyal pets"

# Creating objects
dog1 = Dog("Buddy", 5)
dog2 = Dog.from_birth_year("Max", 2020)
print(dog1.bark())
print(Dog.info())


# ============================================================================
# 2. ENCAPSULATION - Data Hiding & Access Control
# ============================================================================

class BankAccount:
    """Demonstrates encapsulation with private attributes"""
    
    def __init__(self, owner, balance):
        self.__owner = owner  # Private attribute (name mangling)
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        """Public method to modify private data safely"""
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        """Controlled access to private data"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. Remaining: {self.__balance}"
        return "Insufficient balance"
    
    def get_balance(self):
        """Getter method - safe access to private data"""
        return self.__balance
    
    @property
    def balance(self):
        """Property decorator - allows attribute-like access"""
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """Property setter - validates before setting"""
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative")

# Usage
account = BankAccount("John", 1000)
print(account.deposit(500))
print(account.balance)  # Using property


# ============================================================================
# 3. INHERITANCE - Code Reusability
# ============================================================================

class Animal:
    """Base/Parent class"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Cat(Animal):
    """Derived/Child class - inherits from Animal"""
    def speak(self):
        """Override parent method"""
        return f"{self.name} meows"

class Bird(Animal):
    def speak(self):
        return f"{self.name} chirps"
    
    def fly(self):
        """Additional method unique to Bird"""
        return f"{self.name} is flying"

# Multiple Inheritance
class Parent1:
    def method1(self):
        return "From Parent1"

class Parent2:
    def method2(self):
        return "From Parent2"

class Child(Parent1, Parent2):
    """Inherits from multiple parents"""
    pass

child = Child()
print(child.method1())
print(child.method2())

# Usage
cat = Cat("Whiskers")
print(cat.speak())


# ============================================================================
# 4. POLYMORPHISM - Many Forms
# ============================================================================

def animal_sound(animal):
    """Polymorphic function - works with different types"""
    print(animal.speak())

animals = [Cat("Tom"), Bird("Tweety"), Animal("Generic")]
for animal in animals:
    animal_sound(animal)  # Same method calls, different results

# Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        """String representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        """Overload < operator"""
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)
print(v1 - v2)


# ============================================================================
# 5. ABSTRACTION - Abstract Base Classes
# ============================================================================


class Shape(ABC):
    """Abstract base class"""
    
    @abstractmethod
    def area(self):
        """Subclasses must implement this"""
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def info(self):
        """Concrete method in abstract class"""
        return f"Area: {self.area()}, Perimeter: {self.perimeter()}"

class Rectangle(Shape):
    """Concrete implementation"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# rect = Rectangle(5, 10)
# print(rect.info())


# ============================================================================
# 6. METHOD RESOLUTION ORDER (MRO) - Diamond Problem
# ============================================================================

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B -> " + super().method()

class C(A):
    def method(self):
        return "C -> " + super().method()

class D(B, C):
    pass

d = D()
print(d.method())
print(D.__mro__)  # Shows method resolution order


# ============================================================================
# 7. COMPOSITION - Has-a Relationship
# ============================================================================

class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    """Composition - Car has-a Engine"""
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition
    
    def start(self):
        return f"{self.model} started with {self.engine.power}HP engine"

engine = Engine(200)
car = Car("Tesla", engine)
print(car.start())


# ============================================================================
# 8. AGGREGATION - Loose Coupling
# ============================================================================

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        self.employees.remove(employee)

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

dept = Department("Engineering")
emp1 = Employee("Alice", 101)
emp2 = Employee("Bob", 102)
dept.add_employee(emp1)
dept.add_employee(emp2)


# ============================================================================
# 9. SPECIAL METHODS (DUNDER METHODS)
# ============================================================================

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """User-friendly string representation"""
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Returns length"""
        return self.pages
    
    def __iter__(self):
        """Make object iterable"""
        self.current = 0
        return self
    
    def __next__(self):
        if self.current < self.pages:
            self.current += 1
            return f"Page {self.current}"
        raise StopIteration
    
    def __getitem__(self, index):
        """Support indexing"""
        if index == 0:
            return self.title
        elif index == 1:
            return self.author
        raise IndexError("Index out of range")
    
    def __call__(self):
        """Make object callable"""
        return f"Reading {self.title}"

book = Book("Python 101", "John Doe", 300)
print(str(book))
print(repr(book))
print(len(book))
print(book[0])
print(book())


# ============================================================================
# 10. STATIC AND CLASS VARIABLES
# ============================================================================

class Student:
    total_students = 0  # Class variable - shared by all instances
    
    def __init__(self, name):
        self.name = name  # Instance variable
        Student.total_students += 1
    
    @classmethod
    def get_total_students(cls):
        """Access class variable"""
        return cls.total_students
    
    @staticmethod
    def is_valid_name(name):
        """Static method - utility function"""
        return len(name) > 0

s1 = Student("Alice")
s2 = Student("Bob")
print(f"Total students: {Student.get_total_students()}")


# ============================================================================
# 11. PROPERTY DECORATORS - Getters, Setters, Deleters
# ============================================================================

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Convention: _ means private
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @celsius.deleter
    def celsius(self):
        """Deleter"""
        del self._celsius
    
    @property
    def fahrenheit(self):
        """Derived property"""
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)
print(temp.fahrenheit)
temp.celsius = 30
print(temp.celsius)


# ============================================================================
# 12. INSTANCE vs CLASS vs STATIC METHODS
# ============================================================================

class MathUtils:
    pi = 3.14159  # Class variable
    
    def __init__(self, value):
        self.value = value  # Instance variable
    
    def instance_method(self):
        """Works with instance - has access to self"""
        return f"Instance value: {self.value}"
    
    @classmethod
    def class_method(cls):
        """Works with class - has access to cls"""
        return f"Class variable pi: {cls.pi}"
    
    @staticmethod
    def static_method(a, b):
        """Utility function - no access to self or cls"""
        return a + b

math_obj = MathUtils(10)
print(math_obj.instance_method())
print(MathUtils.class_method())
print(MathUtils.static_method(5, 3))


# ============================================================================
# 13. IMMUTABILITY - Immutable Objects
# ============================================================================

class ImmutablePoint:
    """Immutable class - cannot be modified after creation"""
    
    def __init__(self, x, y):
        super().__setattr__('_initialized', False)  # allow setup
        
        self._x = x
        self._y = y
        
        super().__setattr__('_initialized', True)   # lock object
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __setattr__(self, name, value):
        if getattr(self, '_initialized', False):
            print("⚠️ Cannot modify immutable object")
            return
        super().__setattr__(name, value)
    
    def __hash__(self):
        return hash((self._x, self._y))


# Usage
point = ImmutablePoint(1, 2)
print(point.x, point.y)

point.x = 10  # safely ignored

print("Flow continues ✅")


# ============================================================================
# 14. MIXINS - Reusable Functionality
# ============================================================================

class TimestampMixin:
    """Mixin provides timestamp functionality"""
    
    def get_timestamp(self):
        return self.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class LogMixin:
    """Mixin provides logging functionality"""
    def log(self, message):
        return f"[LOG] {message}"

class User(TimestampMixin, LogMixin):
    """Uses multiple mixins"""
    def __init__(self, name):
        self.name = name

user = User("John")
print(user.get_timestamp())
print(user.log("User created"))


# ============================================================================
# 15. DESIGN PATTERNS - Singleton
# ============================================================================

class Singleton:
    """Singleton pattern - only one instance"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - same instance


# ============================================================================
# 16. CONTEXT MANAGERS - With Statement
# ============================================================================

class FileManager:
    """Custom context manager"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        if self.file:
            self.file.close()
        return False

# with FileManager("test.txt", "w") as f:
#     f.write("Hello, World!")


# ============================================================================
# 17. METACLASSES - Classes that create Classes
# ============================================================================

class SingletonMeta(type):
    """Metaclass for creating Singleton classes"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True


# ============================================================================
# 18. DESCRIPTOR PROTOCOL - Property Management
# ============================================================================

class ValidatedString:
    """Descriptor for validated string attributes"""
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, '')
    
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]

class Person:
    name = ValidatedString('name')
    
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.name)


# ============================================================================
# 19. SUPER() - Access Parent Class
# ============================================================================

class Parent:
    def method(self):
        return "Parent method"

class Child(Parent):
    def method(self):
        parent_result = super().method()
        return f"{parent_result} + Child method"

child = Child()
print(child.method())


# ============================================================================
# 20. PRACTICAL EXAMPLE - Complete OOP System
# ============================================================================

class Account(ABC):
    """Abstract account class"""
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
    
    @abstractmethod
    def calculate_interest(self): pass
    
    @property
    def balance(self):
        return self._balance

class SavingsAccount(Account):
    """Savings account with interest"""
    def calculate_interest(self):
        return self._balance * 0.05

class CheckingAccount(Account):
    """Checking account"""
    def calculate_interest(self):
        return 0

class Bank:
    """Bank manages accounts"""
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def get_total_balance(self):
        return sum(acc.balance for acc in self.accounts)

# Usage
bank = Bank("MyBank")
savings = SavingsAccount("John", 10000)
checking = CheckingAccount("Jane", 5000)
bank.add_account(savings)
bank.add_account(checking)
print(f"Total balance: {bank.get_total_balance()}")


print("\n✅ OOP Complete Guide Executed Successfully!")