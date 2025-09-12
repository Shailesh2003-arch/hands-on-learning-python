# This file will hold all the knowledge about 'self' argument (this).

class Chai:
    size = 150

# self refers to the current instance of a class...
# Every function inside the class get's the reference of the current object that's invoking it...
# So you always write 'self' in every method you define inside a class...

    def describe(self, ):
        return f"A {self.size} ml chai cup "


cup = Chai()
print(cup.describe())

# Always remember when you call the methods from the class on an object, it always has the reference which is passed chupke se...
# And when you're calling the method directly from the class, you need to explicitly provide the reference (object) - context ...