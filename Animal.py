class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return 'bark'

class Cat(Animal):
    pass