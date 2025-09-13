# Well this is a mini-project curated using all the learned stuff...

class InvalidChaiError(Exception): pass


def bill(flavour,cups):
    menu = {'masala':20, 'ginger':30}
    try:
        if flavour not in menu:
            raise InvalidChaiError("Chai not available")
        if not isinstance(cups,int):
            raise TypeError("Cup must be a int value")
        total = menu[flavour] * cups
        print(f"Your bill for {cups}  cups of {flavour} chai: rupee {total} ")
    except Exception as e:
        print("Error",e)
    finally:
        print("Thanks for visiting 😁")

# bill("mint",2)
# bill("masala","two")
bill("masala",2)