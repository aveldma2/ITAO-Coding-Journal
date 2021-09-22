import random


class Location:
    def __init__(self):
        self._values = ['woods', 'beach', 'city']
        self._current_value = random.choice(self._values)

    def value(self):
        return self._current_value


class City(Location):
    def __init__(self, *args, **kwargs):
        self._values = ['apartment', 'house']
        self.location_value = random.choice(self._values)

    def value(self):
        return self.location_value


class Woods(Location):
    def __init__(self, *args, **kwargs):
        self._values = ['cabin', 'tent']
        self.location_value = random.choice(self._values)

    def value(self):
        return self.location_value


class Beach(Location):
    def __init__(self, *args, **kwargs):
        self._values = ['beach house', 'hut']
        self.location_value = random.choice(self._values)

    def value(self):
        return self.location_value

