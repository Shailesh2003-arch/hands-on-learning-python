# This file hold all the knowledge about Immutable Object - Tuple. 
# Tuple is an ordered, heterogenous, immutable collection of Python Objects.
# Ordered - The sequence of the elements is fixed.
# heterogenous - Can store any type of python object.
# Immutable - Cannot be modified once created.


# Beautiful is better than ugly. - Formatting.
# Explicit is better than implicit. - somewhere I feel it relatable with 'this' - 'self' of python (Classes/OOPS concepts)
# Simple is better than complex. - Naming conventions.
# Flat is better than nested. avoid mixing things.
# Sparse is better than dense. Keep it simple!
# Readability counts. - code must be readable!... readability === understandability!.
# Errors should never pass silently. can relate with using error handling.
# Now is better than never. - Haha can relate it with the whole life 😁😁
# If the implementation is hard to explain, it's a bad idea. Must know for people interested in startups!.
# Damn ! this Zen actually explain how simple the implementation of python is!...

# Example of creating a tuple and how it can store object of any type.
my_tuple = ("Shaill", 27, 0.11, 3, True, False )

# Example of creating a tuple with Packing how it can store object of any type.
my_tuple = "Shaill", 27, 0.11, 3, True, False 

print(f"You defined a tuple: {my_tuple}")
print(f"Type of the Object:{type(my_tuple)}")

# Example of creating a tuple with Single element.
my_single_ele_tuple = ("Shaill")
print(f"My single element tuple :{my_single_ele_tuple}")

# Example of creating a tuple with no element (empty tuple).
emptytuple = ()
print(f"Your empty tuple is: {emptytuple}")
print(f"Type of the Object:{type(emptytuple)}")


# Accessing elements in the Tuple, is as same as in String, as its also an iterable object. 
# So we can access tuple elements using indexing.

tuple_example = ("Shaill","Ajay", 10, 20,True, False, 3.14) 
print(tuple_example[0])

# Slicing works with tuples. 
print(tuple_example[0:2])

# ********************************** Let's now see some tuple operations. ******************************************** 

# 1) Concatenation (Joins two or more tuples together).

tuple_1 = ("Shaill","Sonali") 
tuple_2 = ("Megha","Nilesh") 
tuple_3 = tuple_1 + tuple_2
print(f"Tuple 3: {tuple_3}")

# 2) Repetion (Repeting a tuple required number of times)

five_times_tuple_3 = tuple_3*5
print(f"Five times we have tuple 3: {five_times_tuple_3}")

# 3) Membership check.
# This operation checks if an element is part of the provided tuple or not, and returns true or false likewise!.

print(f"Shaill in tuple_1 ? {"Shaill" in tuple_1}")
print(f"Vandana in tuple_1 ? {"Vandana" in tuple_1}")
print(f"Vandana not in tuple_1 ? {"Vandana" not in tuple_1}")


# *************************************** Let's now see some tuple methods******************************************** 

# Tuples have only two methods - (count, index)

# 1) count() - returns the count of an element present in the tuple.
numeric_tuple = (10,11,12,13,14,10,20)
print(numeric_tuple.count(10)) # 2

# 2) index() - returns the index of an element with respect to its first occurence.
print(numeric_tuple.index(10)) # 0
