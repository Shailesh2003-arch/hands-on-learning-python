# This file will hold all the knowledge about type-safety in python...
# Well, till date we never made a type check of any data coming into the function or anything stuff like that.
# But today, we will perform type checking of the incoming data, and will only provide result if the data is of valid type...

# There are basically 3 ways how we can perform type-safety in Python...

# 1) Using the builtin method isIstance().
# 2) mypy an external static tool that we run before the runtime process.
# 3) typeguard - an external package which uses decorator to check type-safety.


# 1) Using isInstance():
def sum_numbers(num1:int,num2:int)->int: # these are just type hints... they're just for readability!... doesn't enforces type-safety on runtime...
    if not isinstance(num1,int) or not isinstance(num2,int):
        raise TypeError("Both the argument must be of Type 'int'")
    return num1 + num2

addition = sum_numbers(10.2,20.2) # Providing float params...
print(f"Addition is : {addition}")


# # 2) Using mypy tool.
def sum_numbers(num1:int,num2:int)->int:
    return num1 + num2

addition = sum_numbers(10.2,20.2) # Providing float params...
print(f"Addition is : {addition}")


# 3) Using typeguard package/module....
from typeguard import typechecked

@typechecked
def sum_numbers(num1:int,num2:int)->int:
    return num1 + num2

addition = sum_numbers(10.2,20.2) # Providing float params...
print(f"Addition is : {addition}")













# @typechecked
# def say_hello(name:str)->str:
#     return 1

# stored = say_hello("Shailesh")
# print(stored)

