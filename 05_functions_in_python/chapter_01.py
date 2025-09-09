# This file will hold all the knowledge about functions in python.

# Function is a block of code that performs specific task, it simply means define once and use as much as required!
# function provides readability, modularity and reusability.
# Always remember that a function always returns!... 
# Recieving is optional.

# how we define a function in python ?

# we define a function using the keyword 'def'


def greet():
    print(f"Helloww there!")

# this is how we invoke a function. On invocation the code inside the function gets executed.
# hello = greet()
# print(hello) # If a function does not return anything explicitly, then by default its return type is None.

# def add(x,y):
#     return x + y


# addition = add(3,5)
# print(addition)

# Rest of the thing like parameter and default value is same as the traditional functions.

# Now lets practice some small functionality.

# Assume that we are building an app, where we simply register the user.
# we need to seperate concerns - getting input from the user, validating it, and storing it to the database.

def getUserInput ():
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    gender = (input("Enter Your Gender: "))
    return name,age, gender
    

def validateInput(name,age,gender):
    print(f"{name} name is all good")
    print(f"{age} age is alright")
    print(f"{gender} is ok")
    print(f"Validation completed")


def saveToDB():
    print(f"User suceesfully registered!")

def registerUser():
    # getUserInput()
    validateInput(*getUserInput()) # focus here!...
    saveToDB()

registerUser()