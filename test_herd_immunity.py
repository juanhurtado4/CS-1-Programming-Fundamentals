from person import Person
from virus import Virus
from logger import Logger

import pytest


# TODO: Create a function that initializes virus and person to use
# on all testing funtions
ebola = Virus('ebola', 0.7, 2.5)
person = Person(1, True, ebola)
person2 = Person(2, True)

def test_init_Person():
    # ebola = Virus('ebola', 0.7)
    # person = Person(1, True, ebola)
    # person2 = Person(2, True)
    assert person._id == 1
    assert person.is_vaccinated == True
    assert person.infected == ebola
    assert person2.infected == None

def test_did_survive_infection():
    person = Person(3, False, ebola)
    assert person.did_survive_infection() == False

def test_write_metadata():
    # log = '{}\t{}\t{}\t{}\t{}\n'.format(population_size, vacc_percentage,
    # virus.name, virus.mortality_rate, virus.basic_repro_num)
    population_size = 10
    vacc_percentage = 0.2
    logger = Logger('hello')
    assert logger.write_metadata(10, 0.2, ebola) == '10\t0.2\tebola\t0.7\t2.5\n'
