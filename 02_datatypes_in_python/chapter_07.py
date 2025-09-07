# This file will hold all the knowledge about dictionary in python.

# Dictionary is an unordered, mapping data-type, which stores the data in key-value pairs.
# Where keys are unique and immutable objects like string, number, tuple, etc.
# And values can be any object (Mutable/immutable).

# ways to declare a dictionary.

# 1) using curly braces {}.
student = {
    "name":"Shailesh",
    "lastName":"Thorat",
    "age":21,
    "gender":"Male"
} 
# print(student)
# print(type(student))

# 2) Using dictionary's constructor dict() and kwargs.
my_lifes_dict = dict(name="Shailesh", age=21, dob=27 )
# print(my_lifes_dict)

# 3) Using just the {}
empty_dict = {}
# print(empty_dict)


# Now lets see how we access values present iniside a dictionary.

# print(student["name"])
# print(student["isMarried"])
# print(student.get("isMarried"))

# student_name = student.get("name")
student_name = student["name"]


# Updating existing value.
student["name"] = "Riyansh"
print(student)

# Adding a new value into the dictionary.

student["isMarried"] = False
print(student)


# Deleting a value from a dictionary using del keyword and keyname.
del student["name"]
print(student)

# Deleting a value from a dictionary using pop() and keyname.
student.pop("lastName")
print(student)


# Looping through the keys and printing keys using keys.
for keys in student.keys():
    print(keys)

# Accessing the values of the keys using values().
for value in student.values():
    print(value)

for items in student.items():
    print(items)

# update() - merges another dictionary.

student.update(virgin=True)
# print(student)

student.popitem()
# print(student)


'''
Hashing Concept

Dict keys stored in hash table

Lookup/search/insert is O(1) average

Keys must be hashable (immutable) → string, number, tuple are ok
'''


'''
Common Errors
❌ KeyError: Accessing missing key
❌ TypeError: unhashable type (e.g., using list/dict as key)
'''