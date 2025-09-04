# This file will hold the knowledge about datatypes in python.
# First of all in python everything at the end of the day is an "Object".
# Yess, everything at the end of the day is an Object, whether its an int, float, string, etc.

# Now this Objects are further having a quality that is known as "Mutablity" and "Immutability".

# [Mutable] Objects - Objects that can be updated/which can be changed.

# [Immutable] Objects - Those cannot be changed. (A completely new Object is created whenever a value is changed)   

# Always remember that, mutablity is checked through ID and not the value...

# Example time...

my_score = 10
print(f"Shaill your initial score is : {my_score}")
print(f"Shaill your initial score is : {my_score} and id is : {id(10)}")
my_score = 12
print(f"Shaill your second initial score is : {my_score} and id is : {id(12)}")

# Now here what you can experience is - the value of my_score is getting changed! but that isn't really the thing, as in Python Numbers are immutable, that is they cannot be changed, so what's exactly happening behind the scenes ?...

# What's happening behind the scene is - inside the memory a completely new Object is created with the value 12 and now your reference - my_score is pointing to that Object.