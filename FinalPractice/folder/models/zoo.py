#practice for final

class Animal:
    def __init__(self, name, species, num_legs):
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.favorite_noise = input()

    def give_name(self):
        return self.name

class Tiger(Animal):
    def __init__(self, name, species = 'tiger', num_legs = 4):
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.favorite_noise = ''

    def make_noise(self):
        self.favorite_noise = input('what noise do you make')
        print(self.favorite_noise)





