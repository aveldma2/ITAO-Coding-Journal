import random

class Location:
    def __init__(self):
        self._values = ['woods', 'beach', 'city']
    def choose(self):
        random.choice(self._values)
    def value(self):
        return self._current_value

class City(Location):
    def __init__(self, *args, **kwargs):
        self._values = ['apartment', 'house']
        print(random.choice(self._values))
class Woods(Location):
    def __init__(self, *args, **kwargs):
        self._values = ['cabin', 'tent']
        print(random.choice(self._values))
class Beach(Location):
    def __init__(self, *args, **kwargs):
        self._values = ['beach house', 'hut']
        print(random.choice(self._values))
