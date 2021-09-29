class Person:
    def __init__(self, first, last):
        self._first_name = first
        self._last_name = last

    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def validate(self):
        pass
