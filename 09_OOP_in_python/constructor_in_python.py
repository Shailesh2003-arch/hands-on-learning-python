# This file will hold all the knowledge about constructor in python, which is termed as - __init__ ()
# Constructor ? 
# Construtor is the special function of a class which gets executed as soon as an instance of the class is initiated!..
# What it eventually does is - it initialises your data-members with the provided values...
# like bhai jaisehi object bane - mujhe minimum itna toh object mein chahiye hi chahiye!...

class Chai:
    def __init__(self, type_, size): # this is your constuctor method.
        # yeh hai tumhara constructor joh tumhare bheje hue values se object ko initialise karwa dega!...
        
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.size} chai"
    

order = Chai("Masala",200)
print(order.summary())

order_two = Chai("Ginger",400)
print(order_two.summary())


# For me lets practice about making a class where we send student's name and his age, and the class provides us with the info using the methods...


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_details(self):
        return f"Name of the student:{self.name} and age is {self.age}"


student_1 = Student("Shailesh",22)
print(student_1.student_details())