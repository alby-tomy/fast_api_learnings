import pytest

class Student:
    def __init__(self, first_name:str, last_name:str, age:int, major:str, year:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major
        self.year = year

@pytest.fixture
def student_fixture():
    return Student('Jane', 'Smith', 21, 'Mathematics', 3)