# from pydantic import BaseModel
from typing import List

def sum_list(numbers:List[int]):
    return sum(numbers)


add = [1,2,3,4,5,6,7,8,9,10]
result = sum_list(add)
print(f"After adding all the numbers from the list result is:{result}")
