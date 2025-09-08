# This file will hold the all knowledge about conditionals in python...

# Now what are conditionals ?... 
# Well in programming what we do ? we process data right ?....
# So we process data on certain conditions like if (there's something present in the data then process it further) or else if something is not there, we do some other process.

# That's it, in programming we have various conditions on which we have to trigger some action or process! and that's where conditionals comes in...

# So this conditions always returns the answer in true or false that is yes or no way!...
# And based on that result we decide to take some actions.


# Now we have to display a user if his age is valid to get a driving license or not, for that we have the conditions based on which we will show him/her that if his age is a valid age to get a driving license or not.

# So from the user we wil take input from the user -> input-> age of the user.
# Now we have conditions:
# If user's age is >=18 the user is allowed to get a driving license. 


# taking input from the user in a variable / object age.



# age = int(input("Enter Your Age: "))

# using conditional if statement.

# if age >= 18:
#     print("You are allowed for getting a driving license!")

# Now here this is a conditional statement 'if' which checks if the given data meets the specified criteria ?.
# if yes, then it executes the code mentioned inside the if Block...
# if not, then it skips the execution of if block and moves to the next...

# print(type(age))

# Now let's suppose that if the user dont have the valid age to get a driving license we need to display him a message as you dont have a valid age to get a driving license, age needed to get a driving license is >=18 year's of age.

# Here's when conditional statement else comes in.


# if age >= 18:
#     print("You are allowed for getting a driving license!")
# else:
#     print(f"Minimum age to get a driving license is >=18 years, better luck next time!")


# else conditional statement gets executed when the criteria isnt met by the data... (That is if the conditon isn't satisfied by the data,then else block gets executed...)

# Now there could be multiple conditons based on which you need to perform different actions!...
# And here's when you use elif conditional statement....

# Suppose if the Student gets grade >= 90 you need to show A+ if he gets percentage >=80 then A and likewise...


percentage = int(input("Enter your Percentage: "))

if percentage >= 90:
    print(f"Grade A")
elif percentage >=80:
    print(f"Grade B")
elif percentage >=70:
    print(f"Grade C")
else:
    print(f"Grade D")
    
    
# This is how we use conditonal statements in python to make a decision based on certain criteria...


'''
Truthiness in Python

Condition ka matlab hamesha True/False hota hai.
Python me truthy aur falsy values hoti hain:

Falsy: 0, 0.0, "", [], {}, set(), None, False

Truthy: almost everything else

'''