from person import Person
from virus import Virus

import pytest

# def __init__(self, _id, is_vaccinated, infected=None):

def test_init_Person():
    ebola = Virus('ebola')
    person = Person(1, True, ebola)
    person2 = Person(2, True)
    assert person._id == 1
    assert person.is_vaccinated == True
    assert person.infected == ebola
    assert person2.infected == None
