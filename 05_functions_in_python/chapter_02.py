# This file will hold all the knowledge about scope in python.
# Scope in python is the region of code where a particular name/variable is accessible in the code.


# The reason to learn this scope concept is that - it protects you from many bugs which may be caused because of overwrite of any global variable.

# Anything declared inside a file is known as "Global".

name = "Shailesh" # This is Global.

def greet():
    name = "Riyansh" # This is Local
    print(f"Name inside the function is :{name}")
    def formName():
        nameOnForm = "Abhinav" # this is also the local scope
        nonlocal name
        name = "Mahesh"
        print(f"Name you will get on form is:{nameOnForm}")
        # print(f"But your real name is:{name}")
        print(f"But your real name we manipulated using nonLocal keyword and thus your name now is :{name}")

    formName()

# greet()

# print(f"Name Gloablly is: {name}") # you have written this in global scope, so it first tries to resolve the name into the global scope...



# using nonlocal keyword, we can modify the variable which is declared inside the function.
# and likewise there's a keyword global which you can use to manipulate a global value from inside any function.

chai_type ="Plain"
'''
def serveChai():
    print(f"We serve chai type : {chai_type}")
    def customChai():
        global chai_type
        chai_type = "Kadak Chai"
        print(f"You are getting your custom chai: {chai_type}")
    customChai()

serveChai()'''



# *args gives you a tuple, where as **kwargs gives you a dictionary...
def intro(*self_details,**detailed_info):
    print(f"My details: {self_details}")
    print(f"My detailed info: {detailed_info}")

intro("Shailesh Thorat","21","Male",name="Shailesh", lastname="Thorat", age="22", dob="27/11/2003")


