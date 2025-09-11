# This file will hold all the knowledge about infinte generators in python.

# Now lets understand what is infinite generators...
# Well its nothing more than generating "infinite values on demand", which helps you generate required values without overusing the memory or can say its memory efficient.
# There's nothing much you need to do, just add on a while loop and you're good to go...

# Demo of infinite generator - a dummy sensor generating data, and we're continuously montioring it... 
import time
import random

def sensor():
    while True:
        reading = random.uniform(20.0, 30.0)  # fake temperature
        yield reading
        time.sleep(1)

gen = sensor()

for reading in gen:
     print("Temperature:", reading)