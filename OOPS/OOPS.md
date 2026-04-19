# Object-Oriented Programming (OOPs)

## Overview
Object-Oriented Programming is a programming paradigm that organizes code into reusable objects and classes rather than functions and logic.

## Core Concepts

### 1. **Class**
A blueprint or template for creating objects with specific attributes and methods.

### 2. **Object**
An instance of a class containing state (attributes) and behavior (methods).

### 3. **Four Pillars of OOPs**

#### Encapsulation
Bundling data and methods together while hiding internal implementation details.
  - Helps keeps related fields and methods together
  - Makes our code cleaner and easier to read
  - Provides more flexibility to our code
  - Provides more reusability with our code

#### Inheritance
- Creating new classes from existing classes, promoting code reuse. Process of acquiring properties from one class to other classes
- Creates a hirearchy between classes
  - Method Override : Method overriding is when a child class has its own method already present in the parent class, when the child class does not have the same method, it will default to the parent method




#### Polymorphism
Objects can take multiple forms; same method name behaves differently for different classes. Inshort changing the object at specific runtime

#### Abstraction
Hiding complex implementation and showing only essential features to the user.

## Benefits
- Code reusability
- Better organization and maintainability
- Improved security through encapsulation
- Flexibility through inheritance and polymorphism
- Easier debugging and testing


# Constructors
- Constructors : are used to create and initialize an object of a class with or without starting values

# Self vs Super
 - **self** is used to refer to the current obejct that is created or being instantiated, while **super** is used to refer to the parent class.
 - **self** is used when there is a need to differentiate between the instance variable & parameters with the same name, while **super** is used to call the parent class methos and / or constructors
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Student(Person):
  def __init__(self, name, age, degree):
    super().__init__(name=name,age=age)
    self.degree = degree
```

  - here Student has an extra property : degree
  - Student uses **super** to call Person constructor which assign the properties **name** and **age**
  - Student uses **self** to reference the degree property which is different from the degree parameter /argument coming in.

  - ### Types of Constructor
    - Default/Emty Constructor
    - No Argument Constructor
    - Parameter Constructor


## Example Structure

# What Are We Will Be Creating
## Small game where we can create enimies that fight each other!
- Enimies that can fight one another
- Different types of enimies
  -  Zombie
  -  Orge
  -  Each enemy has difernt poerts health points and attack damage
 

## What do we need to start
Enemy Object 
- Name/Type of Enemy
- Health points
- Attack damage

## Parent Class and Child Class
- Parent Class : Enemy
- Child Class : Zombiee - spred_disease
- Hero Class : health_points, attack_damage, is_weapon_equipped, weapon : Weapon [will HAS_A(composition) relationship with our weapon class]
- Weapon Class : weapon_type, attack_increase

# Composition
- A way to create objects made up of other objects
- In composition, a class contains one or more onjects of another class as instance variables.
- Provide layered functionality to the object
- Known as a HAS-A relationship