# This file will hold the knowledge about how you can handle multiple exception in python...

def process_order(item,quantity):
    try:
         if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
            price = {"masala":20}[item] # here you're extracting the key from the parameter which is you''ll assign to price of the masala...

            cost = price * (quantity)
            print(f"Total cost is {cost}")
            print(f"Price is {price}")
    except KeyError: # if no price is extracted from the key via - key:masala it will go to except block...
        print("Sorry that Chai is not on Menu")
    except TypeError: # if user provides the string value instead of number this exception would be raised...
        print("The quantity must be in Number")

# process_order("ginger",2)
process_order("masala","two")
# process_order("masala",2)