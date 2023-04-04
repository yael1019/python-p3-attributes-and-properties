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
    def set_name(self, name):
        if(type(str)) and (len(name) >= 1 and len(name) <= 25):
            self._name = name
        else:
            print('Name must be string between 1 and 25 characters.')

    name = property(set_name)

# bob = Dog()
# bob.name = 'bob'
# print(bob.name)
