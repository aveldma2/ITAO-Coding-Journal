class Student:
    def __init__(self, name, age):
        self.name = name
        self.id = id
        self.age = age

    def age_validate(self):
        if type(self.age) == int:
            return True
        else:
            return False
