import random


class Children:
    def __init__(self):
        self._values = [1, 2, 3, 4, 5]
        self.num_children = random.choice(self._values)

    def value(self):
        return self.num_children
