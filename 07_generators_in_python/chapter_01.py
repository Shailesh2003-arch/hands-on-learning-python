# Generators in python, this file holds knowledge about generators in python.

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Lemon Chai"


stall = serve_chai()
print(stall)
print(next(stall))
print(next(stall))
print(next(stall))

for cup in stall:
    print(cup)

