# Building an authorisation with decorator...
from functools import wraps

def require_admin(fun):
    @wraps(fun)
    def wrapper(user_roles):
        if user_roles!="admin":
            print("Acess denied: Admin only")
        else:
            return fun(user_roles)
    return wrapper

@require_admin
def access_inventory(role):
    print("Acess granted to tea-inventory")

access_inventory("user")
access_inventory("admin")
