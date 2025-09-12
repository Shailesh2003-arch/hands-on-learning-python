# This file will hold all the knowledge about decorators in python...
# What's a decorator ? ... well as its name suggests, its a decorator which adds on extra stuff on top of your function
# Its a function that takes an argument as a function and returns the wrapper function...

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper


@my_decorator
def greet():
    print("Hello from the decorator")

greet()
print(greet.__name__)
