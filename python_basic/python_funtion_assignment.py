'''
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
'''

def create_person_dict(first_name, last_name, age):
    person_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }
    return person_dict

solution = create_person_dict("John", "Doe", 30)
print("Person dictionary:", solution)