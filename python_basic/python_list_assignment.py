'''
Create a list of 5 animals called zoo
Delete the animals at 3rd index
Append new animal to the list
Delete the animal at beginning index
Print the final list of animals
Print only the first 3 animals in the list
'''


zoo = ["lion", "tiger", "elephant", "giraffe", "zebra"]
print("Initial zoo list:", zoo)

# Delete the animal at 3rd index
del zoo[3]
print("After deleting animal at index 3:", zoo)

# Append new animal to the list
zoo.append("monkey")
print("After appending monkey:", zoo)

# Delete the animal at beginning index
del zoo[0]
print("After deleting animal at index 0:", zoo)

# Print the final list of animals
print("Final zoo list:", zoo)
# using loop to print the animals in the zoo list
for x in zoo:
    print(x)

# Print only the first 3 animals in the list
print("First 3 animals in the zoo:", zoo[:3])