import pytest
from Student import Student

class TestStudent:

    def test_age_num(self):
        s = Student(name = 'John', age = '10')

        assert s.age_validate() == False

    def test_age_not_nothing(self):
        s = Student(name = 'John', age ='')

        assert s.age_validate() == False

    def test_name_str(self):
        s = Student(name = 123, age = 10)

        assert s.name_validate() == False
