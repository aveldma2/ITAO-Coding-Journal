import pytest
import folder.models
from folder.models.zoo import Animal


class TestAnimal:

    def test_name_string(self):
        a = Animal(name = '', species = 'tiger', num_legs = 4)

        assert a.give_name() == False


