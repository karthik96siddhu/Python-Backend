"""
    Instance of a class is called object. That is an object is an entity which as attribute and behaviour. 
"""

class Parrot:
    # class attribute
    name = ''
    age = 0

# creating object parrot1
parrot1 = Parrot()
parrot1.name = 'Blu'
parrot1.age = 10

# create object parrot2
parrot2 = Parrot()
parrot2.name = 'Woo'
parrot2.age = 8

# access attributes
print(f'{parrot1.name} is {parrot1.age} year old')
print(f'{parrot2.name} is {parrot2.age} year old')
