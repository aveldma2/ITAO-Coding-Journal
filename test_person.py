import pytest

class TestPerson:

    def person_has_full_name(self):
        person = Person('Aleida', 'Veldman')
        assert person.full_name == 'Aleida Veldman'

