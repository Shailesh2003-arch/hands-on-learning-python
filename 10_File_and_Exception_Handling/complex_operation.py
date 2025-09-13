# This file will hold essence of  try-except-else-finally  block in error handling...

#  try  block - Write any sensitive code that might have possible chances of failure inside the try-block...

#  except  block - When the code that you tried in 'try-block' fails, then except-block executes, therefore if such exception is caught - handle it gracefully, whatever the handling mechanism you want to write, write it inside the except-block.

#  else  Inside else-block you write the logic that you want to perform if everything went as you expected...

#  finally   Inside finally-block you write the code that must execute no matter exception occurs or everything goes well, finally-block is used to close input streams if any, close the db connections, deallocate the resources allocated for any operation or cleanup the memory. 

def serveChai(flavour):
    try:
        print(f"Preparing {flavour} Chai...")
        if(flavour=="unknown"):
            raise ValueError("We dont know the flavour")
    except ValueError as e:
        print("Error: ",e)
    else:
        print(F"Serving {flavour} Chai...")
    finally:
        print("Next customer!...")

serveChai("Masala") # doesn't throws any error...
serveChai("unknown") # raises an exception...

