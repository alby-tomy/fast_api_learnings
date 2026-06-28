import pytest
from .fixture import Student, student_fixture

def test_equal_or_not_equal():
    assert 3 ==3
    assert 1 != 2
    
def test_is_instance():
    assert isinstance(3, int)
    assert not isinstance('10',int)
    
def test_boolean():
    assert True
    assert not False
    assert ('hello' == 'hello') is True
    
def test_greater_or_less_than():
    assert 3 > 2
    assert 2 < 3
    assert 3 >= 3
    assert 2 <= 3
    
def test_list_membership():
    my_list = [1,2,3,4,5]
    any_list = [False, False, False]
    assert 3 in my_list
    assert 7 not in my_list
    assert all (my_list)
    assert not any(any_list)
    
# pytest object create our python object
        
def test_person_initialization():
    student = Student('John', 'Doe', 20, 'Computer Science', 2)
    assert student.first_name == 'John'
    assert student.last_name == 'Doe'
    assert student.age == 20
    assert student.major == 'Computer Science'
    assert student.year == 2


def test_student_fixture(student_fixture):
    assert student_fixture.first_name == 'Jane'
    assert student_fixture.last_name == 'Smith'
    assert student_fixture.age == 21
    assert student_fixture.major == 'Mathematics'
    assert student_fixture.year == 3