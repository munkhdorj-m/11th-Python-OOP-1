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

    def set_temperature(self, value):
        """Set temperature only if value is between -50 and 150"""
        if -50 <= value <= 150:
            self.__temperature = value
        # else ignore invalid values

    def get_temperature(self):
        """Return current temperature"""
        return self.__temperature

    def increase(self, amount):
        """Increase temperature but not above 150"""
        new_temp = self.__temperature + amount
        if new_temp > 150:
            self.__temperature = 150
        elif new_temp < -50:
            self.__temperature = -50
        else:
            self.__temperature = new_temp

    def decrease(self, amount):
        """Decrease temperature but not below -50"""
        new_temp = self.__temperature - amount
        if new_temp < -50:
            self.__temperature = -50
        elif new_temp > 150:
            self.__temperature = 150
        else:
            self.__temperature = new_temp


