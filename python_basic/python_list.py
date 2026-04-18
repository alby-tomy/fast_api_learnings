# ------------------------------------------------------------
# 12. INTRODUCTION TO LISTS
# ------------------------------------------------------------
# A list is a collection of multiple values stored in one variable.
# Lists are written using square brackets: []
print("\n=== 12. LISTS ===")
fruits = ["apple", "banana", "mango"]
print("List of fruits:", fruits)
print("Type of fruits:", type(fruits))

# Accessing list elements using index
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# Changing an item in the list
fruits[1] = "orange"
print("After changing second fruit:", fruits)

# Adding items to a list
fruits.append("grapes")
print("After append:", fruits)

# Inserting an item at a specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# Removing items from a list
fruits.remove("apple")
print("After remove:", fruits)

# Length of list
print("Number of fruits:", len(fruits))

# Looping through a list
print("Looping through fruits:")
for fruit in fruits:
    print(fruit)

# Checking if an item exists in a list
if "mango" in fruits:
    print("Mango is in the list.")
else:
    print("Mango is not in the list.")



# ------------------------------------------------------------
# 13. FINAL PRACTICE EXAMPLES WITH LISTS
# ------------------------------------------------------------
print("\n=== 13. FINAL PRACTICE EXAMPLES WITH LISTS ===")
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

# Find total using a loop
total = 0
for num in numbers:
    total += num
print("Total of numbers:", total)

# Find average
average = total / len(numbers)
print("Average:", average)

# Simple mixed list example
student = ["John", 18, True]
print("Student list:", student)
print("Name:", student[0])
print("Age:", student[1])
print("Passed:", student[2])


my_list = [80,90,20,1,50]
print("My list:", my_list)


people_list = ["Alice", "Bob", "Charlie", "David"]
print("People list:", people_list)

# slicing
print("First two people:", people_list[0:2])
print("Last two people:", people_list[-2:])
print("All people except first:", people_list[1:])
print("All people except last:", people_list[:-1])


# appending
people_list.append("Eve")
print("After appending Eve:", people_list)

# inserting
people_list.insert(2, "Frank")
print("After inserting Frank at index 2:", people_list)

# removing [removing by value]
people_list.remove("Charlie")
print("After removing Charlie:", people_list)

# popping [removing by index]
popped_person = people_list.pop(2)
print("Popped person:", popped_person)

# length
print("Number of people:", len(people_list))

# looping
print("Looping through people:")
for person in people_list:
    print(person)

# checking existence
if "Alice" in people_list:
    print("Alice is in the list.")
else:    print("Alice is not in the list.")


# sorting
my_list.sort()
print("Sorted my list:", my_list)

people_list.sort()
print("Sorted people list:", people_list)

people_list.append("Alby")
people_list.sort()
print("After appending Alby and sorting:", people_list)