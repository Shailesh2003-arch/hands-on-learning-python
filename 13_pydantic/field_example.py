# This file will hold the knowledge about the advance field type for pydantic.
# pydantic is a schema + validation library, where you provide schema of the incoming data and pydantic provides validation for it...
# Now many a times our data isn't just limited to a single object like string, number, etc.
# It goes beyond that, so with the typing module of python, we can use advance field type and provide it to pydantic's schema.


from pydantic import BaseModel, ValidationError
from typing import List, Dict, Optional

class Cart(BaseModel):
    
    user_id:int
    items:List[str] # when you have a list you gonna have a lot of items in it. So its going to be a list...
                    # Inside the list we have string items...
    quantities:Dict[str,int]



try:
    user_1 = Cart(user_id=121,items=['banana','pineapple','orange'],quantities={'Kgs':200})
    print(user_1)
    print(f"Items added to the Cart!...")
except ValidationError as e:
    print(str(e))


class blogPost(BaseModel):
    title:str
    content:str
    image_url: Optional[str]= None # its optional, if it comes, it will be a string, else it will be None...


    


