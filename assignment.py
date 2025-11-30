# Exercise 1
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0   # private attribute

    def set_grade(self, val):
        # accept only 0–100
        if 0 <= val <= 100:
            self.__grade = val
        else:
            self.__grade = 0   # invalid → reset to 0

    def get_grade(self):
        return self.__grade

# Exercise 2
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
