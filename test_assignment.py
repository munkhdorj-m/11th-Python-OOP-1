import pytest
from assignment import Student

def test1():
    s = Student("Bob")
    s.set_grade(90)
    assert s.get_grade() == 90

@pytest.mark.parametrize("grade", [-1, 150, 999])
def test2(grade):
    s = Student("Test")
    s.set_grade(grade)
    assert s.get_grade() == 0  
    
def test3():
    s = Student("A")
    s.set_grade(50)
    s.set_grade(70)
    assert s.get_grade() == 70
