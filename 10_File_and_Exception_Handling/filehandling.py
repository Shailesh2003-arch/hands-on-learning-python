# This file will hold all the knowledge about file handling in python...

# In day to day life, we all work with text files...
# And heres when the file handling in python comes into the picture...

# With our python program, we can open an exisiting file in our disk, write some data to it and save.
# likewise, for an istance if we want a file (text) file in our working directory we can create one/is automatically created if there doesn't exist any specifid path we provide to open() of file...

# Using open() we can open file through our python programm.

# As opening a file is a sensitive operation, we must use try-except-else-finally block to perform file opening operation...


# try:
#     file = open('order.txt','w')
#     file.write('Hello new content written into the file...\n')
# finally:
#     print("Content successfully written into the file!")
#     file.close()


# Now this above content is wrapped inside the try-except-else-finally block...
# which is manually done by us where we are opening the file and manually releasing the resources !...
# But python provides a keyword 'with' which  automatically do this for us under the hood...
# lets try opening a file using 'with' keyword.


# with open('order.txt','a') as f:
#     f.write(f"New Chai order of - 2 cup Masala Chai")

# Lets try reading the content of a file...
# read() - reads whole content at once...

# with open('order.txt','r') as f:
#     content = f.read()
#     print(content)


# reads specified number of Characters from a file.
# with open('order.txt','r') as f:
#     content = f.read(4)
#     print(content)

# #  readline() reads a line from a file till it meets an end of line.
# with open('order.txt','r') as f:
#     line = f.readline()
#     print(line)


# readlines() - gives you a list of the sentences in the file.
# with open('order.txt','r') as f:
#     lines = f.readlines()
#     print(lines)


try:
    with open("order.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print(f"The file you're trying to read doesn't exists!")