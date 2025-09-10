# This file will hold all the knowledge about comprehension in python.

# syntax:

# for creating a list using comprehension...

nums = [num for num in range(1,11)]
# print(nums)

# for filtering purpose you can provide condition.
evens = [even for even in nums if even%2==0]
# print(evens)

# for transforming...

squares = [square*square for square in nums ]
# print(squares)

names = ["Shailesh","Riyansh","Nahush", "Shailesh", "Nahush"]

titlized = [name.upper() for name in names]
# print(f"Titlised names: {titlized}")

# lets create a set using set comprehension



myset = {name for name in names}
# print(myset)
myset = {name for name in names}
# print(myset)

# lets move towards a little complex thing...
# here we will have to get the unique chais from the dictionary.
recipes = {
    "Masala Chai":["Ginger","Cardmom","Clove"],
    "Elaichi Chai":["Cardmom","Milk"],
    "Spicy Chai":["Ginger","Black Pepper","Clove"],

}

unique_chai = {spice for ingredients in recipes.values() for spice in ingredients}
# print(unique_chai)

# Now lets have a look towards how we can manipulate a dictionary using comprehension

chai_prices_inr = {
    "Masala Chai": 40,
    "Ginger Tea":80,
    "Lemon Tea": 100
}

# Now your task is to convert all of this prices into dollars.

chai_prices_usd = {tea: price/80 for tea, price in chai_prices_inr.items()}
# print(chai_prices_usd)


# generator comprehension...

daily_sales = [5,10,12,7,2,8,10,15,12]

# you want to calculate the sale only if its above 5 rupees.

total_cups = sum((sale for sale in daily_sales if sale>5))
print(total_cups)