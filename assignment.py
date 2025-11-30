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
