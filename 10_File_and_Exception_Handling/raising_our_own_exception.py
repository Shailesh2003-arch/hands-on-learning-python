# lets raise our own exception...

def brewChai(flavour):
    if flavour not in ["masala","ginger","elaichi"]:
        raise ValueError("Chai flavour not available") # raising our custom error... (simple hai)
        # bass constructor ke andar message pass kardo...
    print(f"Brewing :{flavour} chai")


brewChai("mint")

