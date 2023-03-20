"""
Assignment #2: Write a function to reverse a string using recursion (10 mins)
"""

def reverse_s(s: str) -> str:
    if len(s) == 1:
        return s
    return s[-1] + reverse_s(s[:-1])

for s in (
    'asd',
    '123456789',
    'aaaa',
):
    print(reverse_s(s))
