# This is a file that will hold all the knowledge about computed properties from the existing data itself.
# If you want to have any field as a computed field, then first make use of decorator computed_field, and then add @property so that you can actually access this property just like other.
# This file is actually included in the model afterwards.

from pydantic import BaseModel, computed_field

class Product(BaseModel):
    price:float
    quantity:int

    @computed_field
    @property
    def total_price(self)->float:
        return self.price * self.quantity

product = Product(price=50.20,quantity=5)
print((product.total_price))