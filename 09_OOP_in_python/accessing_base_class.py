# This file will contain all the knowledge about how to access base class...
# There are three ways you can access base class inside the derived class
# 1) Code duplication
# 2) Explicit call
# 3) super()

class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
        print("Constructor of base Class executed")

    def printChaiDetails(self):
        return(f"Serving {self.type} with {self.strength} strength")

class GingerChai(Chai): # inherited a base class Chai...
    def __init__(self,type_,strength,spice_level): 
        
    # to acccess the methods and variables of base class we need to execute the constructor of base class from the child class, but here we're probably not doing it, as we're doing code duplication and nothing else...
        
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level

    def serve(self):
        return f"Serving {self.type} with {self.strength} strength and {self.spice_level} spice level"



# my_chai = Chai("Masala Chai","Strong")
# print(my_chai.printChaiDetails())


# my_chai_with_strength = GingerChai("Masala Chai","Strong","Mild")
# print(my_chai_with_strength.serve())


# Second way of accessing the base class using explicit call to the base class's constructor...


class GingerChai(Chai): # inherited a base class Chai...
    def __init__(self,type_,strength,spice_level): 
        Chai.__init__(self,type_, strength) # making an explicit call to base class's constructor...
        self.spice_level = spice_level
    
    def printChaiDetails(self):
        return(f"Serving {self.type} with {self.strength} strength")

my_chai_with_strength = GingerChai("Masala Chai","Strong","Mild")
print(my_chai_with_strength.serve())



# Third way of accessing the base class using super().

class GingerChai(Chai): # inherited a base class Chai...
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
    
    def printChaiDetails(self):
        return(f"Serving {self.type} with {self.strength} strength")

my_chai_with_strength = GingerChai("Masala Chai","Strong","Mild")
print(my_chai_with_strength.serve())



      




        