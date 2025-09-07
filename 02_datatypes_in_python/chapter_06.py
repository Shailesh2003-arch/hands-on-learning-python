# This file will hold all the knowledge about Mutable Object set in Python.

# Set is an unordered, heteregenous, Mutable collection of Objects in Python, where it doesn't allows mutable entites.

'''
Properties

✅ Unordered → indexing/slicing not allowed
✅ Unique → duplicates auto remove
✅ Mutable → new elements add/remove kar sakte ho
✅ Heterogeneous elements allowed (int, str, tuple … but no mutable type like list/dict inside a set)

'''

# Creating a set.

my_set = {10,20,30,30,40, ("Shailesh", "Riyansh"), }
# print(my_set)

# Basic Operation 

# 1) Add - an element can be added using the add() of set.
my_set.add("Riyansh Shukla")

# 2) Remove - an element can be removed using the remove() of set. (Throws an exception if removed element is not present)
my_set.remove("Riyansh Shukla")
# print(my_set)

# 2) Discard - an element can be removed using the discard() of set.
my_set.discard(10)
# print(my_set)

my_set.clear()
# print(my_set)

'''
Set Operations (Mathematical)
Python sets behave like Math sets ✨

'''

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union -> {1,2,3,4,5,6}
print(A & B)   # Intersection -> {3,4}
print(A - B)   # Difference -> {1,2}

