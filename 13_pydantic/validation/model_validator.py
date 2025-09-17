# This file will hold all the knowledge about field validator and model validator...
# We get the Field function to add on extra validation for a field.
# Still if you want to add some custom validation for your field, then you can do so by using  - field_validator.

from pydantic import BaseModel, field_validator, Field, ValidationError, model_validator


class User(BaseModel):
    id:int = Field(...)
    name:str = Field(...,min_length=4, max_length=30)
    age:int = Field(...,ge=0,le=120)
    random_num:int

    @field_validator('random_num')
    def check_random_number(cls,v):
        if v % 2 !=0:
            raise ValueError("You need to enter an even value!")
        return v

input_data = {
    'id':101,
    'age':21,
    'name':"Shailesh",
    'random_num':4
}

try:
    user_one = User(**input_data)
    print(user_one)
except ValidationError as e:
    # print(e.errors())
    print(str(e))
    


class SignupData(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode='after')
    def check_password(cls,values):
        if values.password!= values.confirm_password:
            raise ValueError("Password do not match!")
        return values
    

input_data = {
    'password':"shaill@0708",
    'confirm_password':"shaill@0708"
}

try:
    user = SignupData(**input_data)
    print(user)
except ValidationError as e:
    print(str(e))