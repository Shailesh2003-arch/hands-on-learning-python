# This file will hold all the knowledge about the Mutable Object in Python - List.

# List is an ordered, mutable, heterogenous collection of Python Object.
# Ordered - List maintains the order of the Objects.
# Mutable - List is changeable, that is can be modified (add,update,delete).
# Heterogenous - Can store any type of Object (Mutable as well as Immutable).


# Lets see how to create list in python.
# list is denoted using [] (square bracket notation).


# using [] notation.

my_shopping_list = ["Perfumes", "Trimmer", "Fruits"]
# print(f"Your shopping list is :{my_shopping_list}")

# using list constructor. 
my_list = list((10,20,30))
# print(f"You defined list: {my_list}")

# we can create en empty list using []
empty_list = []
# print(empty_list)

# Accessing a list [As it's an iterable object we can access it using indexing].

# print(my_shopping_list[0])

# we can modify a list.
my_list[0] = 50 # overwriting the value on the first index.
# print(f"You defined list and its id is: {id(my_list)}") 
# print(f"You defined list and its id is: {(my_list)}")
# print(f"You defined list and its id is: {id(my_list)}")

# After comparison you'll find both the IDs same, that's what known as Mutable.

# Now lets see some methods of List...

# ***************************************** Inserting element methods ***************************************** 


# append() - adds an element to the end pf the list.
my_list.append("Shailesh")
print(my_list)

# insert() - inserts an element at the specified position in the list.
my_list.insert(1,"Megha")
print(my_list)

my_list.extend(["Nilesh","Sonali", "Vandana", "Shailesh"])
print(my_list)

# ***************************************** Element removing methods ***************************************** 

# remove() - Removes an element's first occurence in the list.

my_list.remove("Shailesh")
print(my_list)

# pop() - Removes the last item from an element by default. If specified index, removes the element present on that index.

my_list.pop() # removes Shailesh
my_list.pop(1) # removes Megha
print(my_list)

# clear() - Removes all the elements/objects from the list and returns an empty list.
# my_list.clear();
# print(my_list)


# ******************************** Element Searching and Frequency checking methods ******************************


# index() - Returns the index of specified Object in the list.
indexofShailesh = my_list.index("Shailesh")
print(indexofShailesh)

# count() - Returns the count of occurence of specified Object in the list.
count_of_shailesh = my_list.count("Shailesh")
print(count_of_shailesh)



# ******************************** Element sorting and reversing methods *******************************************

unsorted_list = [40,50,10,5,10]
unsorted_list.sort();
print(unsorted_list)

unsorted_list.reverse()
print(unsorted_list)

# copy() - returns a new instance of the copied list, whereas, direct assignment points to the same object.
newList = my_list.copy();
print(f"Id of the original list: {id(my_list)}")
print(newList)
print(f"Id of the copied list: {id(newList)}")