# This file will hold the knowledge about yield from and close in generators...

# Well this yield from and close is nothing but, yield from says : "Bhai yeh chiz is generator se aajayegi - yield hojayegi" and close - gracefully closes the generators - just like a cleanup which makes sure that theres no memory leak chances and no memory crash...

# lets make a generator...

def subgen():
    yield 1
    yield 2
    yield 3

def main_gen():
    print("Yielding started")
    yield from subgen()
    print("Done yielding the values")


g = main_gen()

for val in g:
    print(val)


'''
Real life use:

Pipeline / workflow banate waqt — ek bada generator chhote chhote sub-tasks ko delegate karta hai.

Example: ek "data pipeline generator" → uske andar ek "cleaning generator", ek "augmentation generator", ek "normalization generator". Sabko yield from se attach kar de, and tu ek hi flow mein data consume kar lega.
'''


# Now lets see about close...
# close is a method which is used with the generator object to gracefully shutdown the generator.


def gen():
    try:
        userInput = yield "Waiting for user's input!"
    except:
        print("Didn't got any input shutting down the generator")


g = gen()
print(next(g))
g.close() # shutting down the generator gracefully...