# Well, now its the right time to know how to handle the errors in our code!...
# We know that, in the real world, the code might fail due to various reasons - unavailability of the resource, server down, or whatever the reason may...

# for example: lets demonstrate a small error...

# declaring a list of numbers...

numbers = [item for item in range(1,11)]

# Now see that, we're trying to access - an item which is on index 11 which is not even present in the list which will obviously throw us some error...

# print(numbers[11]) # Raises keyError

# Now this line of code wont get executed, as the line above this threw an error...
# Resulting into a crash of our application.
# print("Next lines of code...")

# Now lets write this code in such a way that if this kind of error occurs, then it doesn't crashes our app instead,
# it gracefully handles that error, saving our app from being crashed!...

# for that we use try-except block...

try:
    print(numbers[11])
except IndexError:
    print(f"The index you're trying to access doesn't exists!")

print("Next lines of code...")

# So this is how we handled the error gracefully without letting our application being crashed...


