"""
Sets are similar to lists but they are unordered and do not allow duplicate elements. They are defined using curly braces {} or the set() constructor.
"""

my_set = {1, 2, 3, 4, 5, 5, 3}  # Duplicate values will be ignored
print("My set:", my_set)


for x in my_set:
    print(x)

#  while using set python automattically allocate the memory for the values randomly and it is not in order as list. 
# so we can not access the values by index like list. we can only access the values by looping through the set or 
# by using the in keyword to check if a value is present in the set.


# to remove the element
my_set.discard(3)
print("After discarding 3:", my_set)

my_set.clear()
print("After clearing the set:", my_set)

my_set.add(10)
print("After adding 10:", my_set)

# adding multiple elements to the set
my_set.update([20, 30, 40])
print("After updating the set with multiple values:", my_set)
