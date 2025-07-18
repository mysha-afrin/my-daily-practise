import random ,string
from math import floor
from random import * #This code imports all functions from the random module

random_number = random.randint(1, 10)# This code generates a random integer between 1 and 10
print(random_number)

test_list = ['hello', True, [1, 2, 3], 6, 8]
print(random.choice(test_list))  # This code randomly selects an element from the list
print(string.ascii_letters)  # This code prints all ASCII letters (both lowercase and uppercase)
print(floor(4.9))
