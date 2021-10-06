#practice for final

class Animal:
    def __init__(self, name, species, num_legs):
        self.name = name
        self.species = species
        self.num_legs = num_legs

    def give_name(self):
        return self.name


a = Animal(name = 'Bob', species= 'dog', num_legs= 4)

print(a.give_name())

