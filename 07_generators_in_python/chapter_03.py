# Now this file will hold the knowledge about sending data to the generator.
# Yess!... you can send data to the generators.


# lets define a simple generator function...


def chai_customer():
    print ("Welcome ! what type of chai would you like to have ?") # it executes this line
    print("Print kar raha hu aisehii, maja aaraha hai 😂😂")
    print("Print kar raha hu aisehii, maja aaraha hai 😂😂")
    order = yield # and waits for any value to be recieved here. if not recieved, then it terminates.
    while True: # loop - for contiuous (infinite generation of value)
        print(f"Preparing {order} for you!...")
        order = yield
    

chai = chai_customer()
next(chai) # executes the code of lines till it meets yield.

chai.send("Masala chai") # sends value to the yield...
chai.send("Ginger chai") # sends value to the yield...



# Filtering text data using the generator...
def text_filter():
    while True:
        text = yield
        print("Cleaned:", text.strip().lower())
        
g = text_filter()
next(g)
g.send("   Hello BRO   ")  # "hello bro"
g.send("   PYTHON   ")     # "python"
g.send("   RIYANSH   ")     # "riyansh"