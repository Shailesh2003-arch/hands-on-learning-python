# This file will hold all the knowledge about inheritance and composition in python.

class BaseChai:
    def __init__(self, type_):
        self.type = type_
    

    # construtor
    def prepare(self):
        print(f"Preparing {self.type} chai...")


class MasalaChai(BaseChai): # you only use () in class in python when you want to inherit something.
    def add_spices(self):
        print("Adding cardmom, ginger, cloves.")


# lets now see how composition works!...

class ChaiShop:
    chai_cls = BaseChai # holding the reference of the whole base class...
    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.chai.add_spices()