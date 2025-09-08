# This file will hold all the knowledge about loops in python...

# Why do we need loops ?...
# We need to perform certain operation number of times, that's where we use loop.

# lets start of with for loop...

# Now how we loop through any iterable ?
# we use a keyword 'for' then we use a variable to itereate over an iterable and then we use the iterable name on which we want to iterate...


# In python for loop iterates only on the iterables, you dont need to manually increment or initialise any value...


for token in range(1,11):
    print(f"Serving chai to token #{token}")

# here range() is an iterable -> a sequence Object which generates number from a specified range to a specified range where the last_range is exclusive.

for number in range(1,11,2):
    print(number)


