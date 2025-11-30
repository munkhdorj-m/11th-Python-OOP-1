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
class TemperatureSensor:
    def __init__(self, name):
        self.name = name
        self.__temperature = 0  # private attribute

    def set_temperature(self, temp):
        # Only allow realistic temperatures between -50 and 150 Celsius
        if -50 <= temp <= 150:
            self.__temperature = temp
        else:
            self.__temperature = 0  # default if invalid

    def get_temperature(self):
        return self.__temperature

