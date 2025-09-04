# Now let's write some mutable objects...
# Here we will write some mutable objects that can be changed! that means the object will get updated.


# list,set and dictionary are mutable objects in python, that means they can be changed.
# lets take an example of list...

# created an object of list...
ls = [1,2,3,4]
print(ls)
# printing its id...
print(f"Id of this list is: {id(ls)}")

# adding new data to the list... 
# (as its mutable it should change in the existing list itself and not create a new intance and point to that)
ls.append(5)
print(ls)
# printing the id to check if its the same list. (Yess, it is!)
print(f"Id of this list is: {id(ls)}")