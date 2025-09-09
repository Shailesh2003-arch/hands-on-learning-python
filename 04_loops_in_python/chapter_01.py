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
# Also note that, range()'s third parameter is step - so it skips the specified number of steps.

for number in range(1,11,2):
    print(number)



names = ("Shailesh","Nilesh","Megha", "Sonali")
for users in names:
    print(users)


# Now lets move towards enumerate() it helps you to print the index number.

for idx, user in enumerate(names, start=1):
    print(f"{idx}: {user}")


# ls = list(range(1,11,2))
# print(ls)

names = ("Shailesh","Ravi","Pavan","Max")
bills = [50,45,60, 75]

for name,amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")

# for name in names:
#     print(name)

# print(names)

zippedOne = zip(names,bills)
# print(zippedOne)

# print(list(zippedOne))

# lets understand while loop in python...
# while loop provides control in python, it lets you control the loop using break and continue clause/statement.

# lets see an example:

num = 1
while num<=10:
    print(num)
    num+=1

# controlling the flow using break and continue.

while num <= 10:
    if num ==3:
        num+=1
        continue
    print(num)
    num+=1

# Also know that theres a fallback as else in for loop.



