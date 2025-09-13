# This file will hold all the knowledge about - class methods in python...
# What are class-method?...
# A method that belongs to the class and can manipulate the class-level data as well as can acts as an altearnate constructor for initialising the objects.

# To use and define a class method you just need to add on a decorator above the method as @classmethod.

class ChaiShop:
    # Here this is a normal constructor...
    def __init__(self, chai_type, sweetness, size):
        self.chai_type = chai_type
        self.sweetness = sweetness
        self.size = size
    
    def __str__(self):
        return f"{self.chai_type} {self.sweetness} {self.size}"


    # Now there might be a chance that someone provides you value of an object in the dictionary format/string format, then how you gonna handle it?...
    # Here's when class-method shines ✨

    @classmethod
    def dict_form(cls, order_data):   # this method gets the reference of the class itself.
        return cls(
            order_data["chai_type"],
            order_data["sweetness"],
            order_data["size"],
        ) # when you do this - it means that you're passing the whole value to the class's construtor behind the scenes.
    



    @classmethod
    def string_form(cls, order_data):   # this method gets the reference of the class itself.
        chai_type, sweetness, size = order_data.split("-")
        return cls(
            chai_type, sweetness, size
        ) # when you do this - it means that you're passing the whole value to the class's construtor behind the scenes as a string.
    

chai_1 = ChaiShop.dict_form({
    "chai_type":"Masala Chai",
    "sweetness":"Low",
    "size":"Medium"
})


chai_2 = ChaiShop.string_form("Ginger_Chai-Low-Medium")

print(chai_1.__dict__)
print(isinstance(chai_1,ChaiShop)) # checking if its an instance of the class we made.

print(chai_2)
print(isinstance(chai_2,ChaiShop)) # checking if its an instance of the class we made.
