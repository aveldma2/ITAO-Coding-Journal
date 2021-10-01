import pytest
from Student import Student

class TestStudent:

    def test_age_num(self):
        s = Student(name = 'John', age = '10')

        assert s.age_num() == False

