#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = 'fido'):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self, name):
        if isinstance(name, str) and len(name) >= 1 and len(name) <= 25:
            self._name = name
        else:
            print('Name must be string between 1 and 25 characters.')

    name = property(get_name, set_name)

# bob = Dog()
# bob.name = 'bob'
# print(type(bob))
