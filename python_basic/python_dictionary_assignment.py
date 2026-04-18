"""
Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values
- Create a new variable vehicle2, which is a copy of my_vehicle
- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- Delete the mileage key and value from vehicle2
- Print just the keys from vehicle2
"""

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

# Create a for loop to print all keys and values
for key, value in my_vehicle.items():
    print(key, value)

# create a new variable vehicle2, which is a copy of my_vehicle
my_vehicle2 = my_vehicle.copy()

# Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
my_vehicle2['number_of_tires'] = 4

# Delete the mileage key and value from vehicle2
my_vehicle2.pop('mileage')

# print the keys from vehicle2
print("Keys in vehicle2:", my_vehicle2.keys())

for key in my_vehicle2:
    print(key)