# This file will hold all the knowledge about Custom Exception in python...

class OutOfIngredients(Exception): # when you dont define a constructor in the child class, then base class ka constructor free mein execute hojata hai...
    pass


def brewChai(milk, water):
    if milk == 0 or water == 0:
        raise OutOfIngredients("Milk or water quantity is 0")
    print(f"Brewing chai with {milk} cups of milk and {water} cups of water")
        
brewChai(0,1)
brewChai(2,2)
