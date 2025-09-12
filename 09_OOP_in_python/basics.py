# This file will hold all the knowledge about OOPs in python, well OOPs is nothing but a program paridgm...
# A style of writing program...
# OOPs deals with objects...
# We know that in python everything is an Object, so eventually, Class is also an object...

# Well Class is just a blueprint.
# A class contains of data members (variables) and member functions (methods).

# lets create our first Class...
# When we declare variables inside a class they're called as 'Properties'


class Chai: # defined a class, with the class keyword
    origin = "India" # declared a property.

# print(Chai.origin) # We can access the property inside the class using class_name and . operator.

Chai.is_hot = True # We can add properties into a class using the same syntax - class_name and . operator.

# print(Chai.is_hot) # Successfully added the property into class Chai.

# Each instance of a class has access to all the properties and methods defined inside a class.
# let's instiantiate an object of class Chai.

first_chai = Chai() # instantiated an object of class Chai...
# print(first_chai.is_hot) # It has access to all the properties of class Chai...

first_chai.is_hot = False # You modify the value inside your instance doesn't affect the value inside the class...
# print(first_chai.is_hot) # False
# print(Chai.is_hot) # True

first_chai.flavour = "Masala" # You can add on more properties to an instance instantied from a class and wont affect the original class...
print(first_chai.flavour)