# Here this file will hold knowledge about datatype such as Number...

# In python Numbers are also an "Object"... An [Immutable] Object...

# In Number category we have 4 big players...
# 1) Integers -> Integer represents whole number, without decimal...
# 2) Float -> Floating point numbers which contians decimal...
# 3) Complex Numbers -> Numbers that are imaginary + real.
# 4) Booleans (bool) -> True and False are also technically Number.


# Basically all these are classes, that is int, float, complex and bool you can check it by using the method like
# int() float() bool() complex() you'll get that these are classes. 

# Some example...

x = 10
y = x+1
# print(f"Value of y is: {y}")

isLoggedIn = True
x = 5 + isLoggedIn # typecasting happens here!...
print(f"Value of x is : {x}") # And thus it results into 6.

# Now lets see some stuff about logical operator and logical operation.

# What is logical operation ?
# Logical operations are processes that connect or modify true/false statements/values to produce a single true or false result.

# In python we have 3 logical operators.
# 1) and
# 2) or
# 3) not

# 1) and results into true only when both input value are true...

isStudent = True
isFeesPaid = True

isAllowed = isStudent and isFeesPaid
# print(f"Is Shaill allowed for the workshop: {isAllowed}")

# 2) or results into true if any one of the input value is true...

chai = True
cofee = False

myPreferredDrink = chai or cofee
# print(f"I can have any one of the tea or coffe :{myPreferredDrink}")

# 3) not operator negates the boolean value.
likeChai = True
print(f"Do you like Chai ? :{not likeChai}")

