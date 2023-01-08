
class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = 'Mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


dog1 = Dog(breed = 'Lab', name='Dickey')
print(type(dog1))
print(dog1.breed, dog1.name, dog1.species)

dog2 = Dog('Hukie', 'Tom')
print(dog2.breed, dog2.name)

import math

class Circle():
    pi = math.pi
    def __init__(self, radius = 1):
        self.radius = radius
    def area(self):
        return (self.pi)*(self.radius**2)

circle = Circle(radius = 2)
print(circle.area())
