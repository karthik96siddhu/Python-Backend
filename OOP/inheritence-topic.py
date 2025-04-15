"""
    Inheritence is a way of creating new class for using details of existing class without modify it.
"""

# base class
class Animal:

    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I can sleep")
    
# derived class
class Dog(Animal):

    def bark(self):
        print("I can bark")

# create Object of Dog class
dog = Dog()

dog.eat()
dog.sleep()
dog.bark()
