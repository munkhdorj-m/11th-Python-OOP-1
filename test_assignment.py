import pytest
from assignment import Student,BankAccount

def test1():
    s = Student("Bob")
    s.set_grade(85)
    assert s.get_grade() == 85
    s.set_grade(150)
    assert s.get_grade() == 0
    with pytest.raises(AttributeError):
        _ = s.__grade
    assert s.name == "Bob"

def test2():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    assert acc.get_balance() == 150
    acc.withdraw(30)
    assert acc.get_balance() == 120
    acc.withdraw(200)
    assert acc.get_balance() == 120
    acc.deposit(-10)
    assert acc.get_balance() == 120
