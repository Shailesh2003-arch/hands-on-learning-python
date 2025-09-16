# Pydantic is a schema + validation library which allows you to define the schema for incoming data, as well as 
# it also provides you with validation...

# 1) While working with pydantic, always use BaseModel class inherit it into your defined class.
# 2) Provide type annotations.
# 3) For creating the objects, always use unpacking of the dictionary.
# 4) When you create an instance pydantic validates each and every field. if something that's convertible it will get converted like if expected data-type is int and you pass '1' it will get converted into number type...

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id:int
    name:str
    is_active:bool


input_data = {'id':'1', 'name':"Shailesh",'is_active':False}


try:
    user_one = User(**input_data)
    print(user_one)
except ValidationError as e:
     print(e.errors())
     print(str(e))


