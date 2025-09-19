# This file will contain the knowledge about nested model in pydantic.
# Nested model allows you to compose complex data structure by embedding one pydantic model inside other pydantic model.

from pydantic import BaseModel, ValidationError
from typing import List, Optional


class Address(BaseModel):
    street:str
    city:str
    zipcode:str


class User(BaseModel):
    id:int
    name:str
    address:Address


address = {
    'street':"Luminous street",
    'city':"London",
    'zipcode':"431001"
}


try:
    user = User(id=101, name="Shailesh", address=address)
    print(user)
except ValidationError as e:
    print(str(e))
