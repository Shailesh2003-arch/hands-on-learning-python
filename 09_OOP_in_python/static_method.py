# This file will hold all the knowledge about static method in a class.
# Which is created using the decorator @staticmethod and it becomes a static method of the class.
# Static method dont need an object to be instantiated to be called.
# You can simply call the static method with the class name.


class ChaiUtils:
    @staticmethod
    def cleanItems(text):
        return [item.strip() for item in text.split(",")]


raw = "Chai  , Sugar,  Tea-leaves, Water"

cleanedItems = ChaiUtils.cleanItems(raw)
print(cleanedItems)