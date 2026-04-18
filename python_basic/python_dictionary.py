"""
Dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
"""

user_dictionary = {
    'username ': 'john_doe',
    'name' : 'John Doe',
    'age' : 30,
}

print(user_dictionary.get('username'))  # Output: john_doe
print(user_dictionary.get('name'))      # Output: John Doe
print(user_dictionary.get('age'))       # Output: 30

user_dictionary["married"] = True
print(user_dictionary)

print("length of dictionary:", len(user_dictionary))

# pop
popped_value = user_dictionary.pop('age')
print("Popped value:", popped_value)
print("After popping age:", user_dictionary)

# popitem
popped_item = user_dictionary.popitem()
print("Popped item:", popped_item)
print("After popping an item:", user_dictionary)

# clear
user_dictionary.clear()
print("After clearing the dictionary:", user_dictionary)

# delete
del user_dictionary
print("After deleting the dictionary:", user_dictionary)

user_dictionary = {
    'username ': 'john_doe',
    'name' : 'John Doe',
    'age' : 30,
}
for key, value in user_dictionary.items():
    print(key, value)  # prints the keys and values

user_dictionary2 = user_dictionary
user_dictionary2.pop('age')
print("After popping age from user_dictionary2:", user_dictionary)

# copying the dictionary
user_dictionary = {
    'username ': 'john_doe',
    'name' : 'John Doe',
    'age' : 30,
}
user_dictionary3 = user_dictionary.copy()
user_dictionary3.pop('age')
print("After popping age from user_dictionary3:", user_dictionary3)
print("Original user_dictionary:", user_dictionary)