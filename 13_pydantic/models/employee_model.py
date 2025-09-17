from pydantic import BaseModel, Field, ValidationError, constr
from typing import Optional


# Dekh bhai Field function ko call karke extra validation laga sakte hai kisi bhi filed pe...😂😂
# Most commonly used hai required joh ... se represent karte hai, then comes min_length, max_length,description,example, ge, le.
# joh bhi field ke liye extra validation chahiye wha pe open karna fieldname:expected_type = Field( yaha pe de dena required validation)

# class employee(BaseModel):
#     id:int
#     name:str = Field(
#         ...,
#         min_length=3,
#         max_length=50,
#         description="Employee Name",
#         examples="Shailesh Thorat"

#     )

#     department:Optional[str] = 'General'
#     salary:float = Field(
#         ...,
#         ge=10000
#     )

# emp_data = {'id':101,'name':"Sh",'salary':95000.00}

# try:
#     emp_1 = employee(**emp_data)
#     print(f"Employe details are : {emp_1}")
# except ValidationError as e:
#     print(ValidationError(e))
#     print(str(e))


class RegisterUser(BaseModel):
    name:str = Field(..., min_length=5, max_length=30)
    # email: #reg
    age:int = Field(...,ge=0, le=120)
    mobile: constr(pattern=r'^\d{10}$')
    address:str = Field(..., description="Enter your complete resedential address")


user_data = {
    'name':"Shailesh Thorat",
    'age':12,
    'mobile':"9156915861",
    'address':"H.No:403, Eknath Nagar, Osmanpura Aurangabad."
}

try:
    register_user_one = RegisterUser(**user_data)
    print(register_user_one)
except ValidationError as e:
    print((e.errors()))
    print(str(e))