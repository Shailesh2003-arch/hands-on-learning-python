# This file will hold all the knowledge about Attribute Shadowing in python...
#  Attribute ~ variable
# When you assign any value to the instance's attribute and later delete it, but in the class you already had a value specified, then it fallbacks to that class's value is what known as "Attribute-Shadowing"

class Chai:
    temperature = "hot"
    strength = "strong"


cutting_chai = Chai()
print(cutting_chai.temperature)

cutting_chai.temperature = "Mild"
print(f"After changing instance's value: {cutting_chai.temperature}")
print(f"Directly accessing attribute's value from Class Chai : {Chai.temperature}")

# adding one more property into the instance itself.
cutting_chai.cup = "small"
# deleting the assigned value of cutting chai...
# using del keyword we can delete the property we assigned to any instance...

del cutting_chai.temperature
print(f"After deleting instance's value's property:{cutting_chai.temperature}")
del cutting_chai.cup
print(cutting_chai.cup)
