# This file hold all the knowledge about String Object...

# String is also an Immutable datatype in python, that is you change it, a completely new object is created.

name = "Shaill"
print(f"My name is:{name}") 
print(f"Id of name is: {id(name)}")

capitalized = name.capitalize()
print(f"Capitalised name is:{capitalized}")
print(f"Id of capitalised name is: {id(capitalized)}")

# Concatenation of strings....
print('Hello ' + 'World')


# Some commonly used string methods...

# **************************************** Case Conversion ********************************************
myName = "Shailesh"

# 1) upper() - Transforms the String into uppercase.
nameInUpperCase = myName.upper()
print(f"My name in uppercase: {nameInUpperCase}")

# 2) lower() - Transforms the String into lowercase.
nameInLowerCase = myName.lower()
print(f"My name in lowercase : {nameInLowerCase}")

# 3) capitalise() - Transforms the First letter of the String into Uppercase.
nameInCapitalCase = myName.capitalize()
print(f"My name in Capital Case : {nameInCapitalCase}")

# 4) title() - Transforms each words First letter into Uppercase.
nameInTitleCase = myName.title()
print(f"My name in Title Case : {nameInTitleCase}")

# 5) swapcase() - Transforms lowercase letters to uppercase and vice-versa.
nameInSwapCase = myName.swapcase()
print(f"My name in Swap Case : {nameInSwapCase}")

# **************************************** Whitespaces and Cleaning *******************************************

fullName = "  Shailesh Thorat "

# 1) strip() - Removes starting and trailing whitespaces...
FullName = fullName.strip()
print(f"My full name is: {FullName}")

# 2) lstrip() - Removes whitespaces from the left side of the string...
LeftSideTrimmed = fullName.lstrip()
print(f"After removing whitespaces from left side, my name is: {LeftSideTrimmed}")

# 3) rstrip() - Removes whitespaces from the right side of the string...
RightSideTrimmed = fullName.rstrip()
print(f"After removing whitespaces from right side, my name is: {RightSideTrimmed}")



# **************************************** Search and Check *******************************************

# 1) startswith() - checks if a string starts with the provided substring.
starts_with = fullName.startswith("  Sha")
print(starts_with)


# 2) endswith() - checks if a string ends with the provided substring.
ends_with = fullName.endswith("  Sha")
print(ends_with)

# 3) find() - gives you the index of provided substring.
indexOf = fullName.find("ha")
print(indexOf)

# 4) count() - gives you the count of occurrence of a provided substring.
countofsubs = fullName.count("h")
print(countofsubs)


# **************************************** Replace and Modify *******************************************


# 1) replace() - Replaces a substring with another one.
replaceThoratWithJhorat = fullName.replace("Thorat","Jhorat")
print(f"Thorat now became: {replaceThoratWithJhorat}")

# 2) split() - Splits a string into an iterable list.
listFromString = fullName.split(",")
print(listFromString)
