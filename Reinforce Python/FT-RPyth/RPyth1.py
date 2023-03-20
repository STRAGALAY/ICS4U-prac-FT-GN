"""
Assignment #1: Write a function that takes a list and checks if there are any duplicates (8 mins)
"""

from typing import TypeVar
T = TypeVar('T')

def check_dupe(lst: list[T]) -> bool:
    elements = set()

    for element in lst:
        if element in elements:
            return True
        elements.add(element)

    return False

print(check_dupe(
    [1,2,3,4,5]
))
print(check_dupe(
    [1,2,3,4,5,6,6]
))
