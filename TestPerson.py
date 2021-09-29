import pytest
from Person import *

class TestPerson:
    def test_name_nonnumeric(self):
        p = Person('1234')
        assert p.validate() == False
