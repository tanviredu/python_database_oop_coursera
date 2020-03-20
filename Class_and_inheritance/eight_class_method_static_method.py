##
## class method isa method that is bund to the class
## not the object  you can call this function without instantiate it
## it will take "cls" as a parameter
## you can use the self too 
## its just traditional that we use the cls
## for the 
## the main target is using the method
## without even instantiate the class
from datetime import date
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    ### create a class method
    @classmethod
    def fromBirthyear(cls,name):
        print ("hello {}".format(name))

Person.fromBirthyear("tanvir")






## static method


class MyClass:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printEveryThing(self):
        print ("name is {} and age is {}".format(self.name,self.age))


    @staticmethod
    def welcome():
        return "hello !! wwelcome to the bank"


cls = MyClass("tanvir",22)

cls.printEveryThing()
print(MyClass.welcome())




### whats the purpose of these two
### is the same that using the method with instantiate the class
## you can do that with these two
## but still the @classmethod takes an argument just like self
## you can use self if you want insted of cls
## but in the @staticmethod you dont have to use the self key word
## class method can modify class state we will talk about it later
## static method dont even know that what happen outside the class
