from person import Person
from virus import Virus

import pytest

# def __init__(self, _id, is_vaccinated, infected=None):

def test_init_Person():
    ebola = Virus('ebola', 0.7)
    person = Person(1, True, ebola)
    person2 = Person(2, True)
    assert person._id == 1
    assert person.is_vaccinated == True
    assert person.infected == ebola
    assert person2.infected == None

def test_did_survive_infection():
    hiv = Virus('hiv', 0.012)
    person = Person(3, False, hiv)
    assert person.did_survive_infection() == True
