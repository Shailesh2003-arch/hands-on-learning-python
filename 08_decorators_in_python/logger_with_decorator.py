# Building a logging decorator...

from functools import wraps

def log_activity(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        print(f"🚀 Calling function {fun.__name__}")
        result = fun(*args,**kwargs)
        print(f"☑️  Finished {fun.__name__}")
        return result
    return wrapper  

@log_activity
def brew_chai(type):
    print(f"brewing {type} Chai")

brew_chai("Masala Chai")
