import pytest
from assignment import Student

def test1():
    s = Student("Bob")
    s.set_grade(85)
    assert s.get_grade() == 85
    s.set_grade(150)
    assert s.get_grade() == 0
    with pytest.raises(AttributeError):
        _ = s.__grade
    assert s.name == "Bob"
