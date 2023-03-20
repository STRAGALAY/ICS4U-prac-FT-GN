"""
Write a RandomAlphabet class where the constructor takes no arguments, and has an
‘alphabet’ attribute that is a dictionary structured as (c: n) where c is an 
alphanumeric character in string form, and n is a random number in [1, 100] inclusive.
(12 mins)
"""

import random

class RandomAlphabet:
    def __init__(self):
        self.alphabet = {
            chr(c): random.randrange(0, 101)
            for c
            in range(ord('a'), ord('a') + 26)
        }

print(RandomAlphabet().alphabet)
