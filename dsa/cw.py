# this is a python program for a random quote generator
"""
import random
create a list of different quotes
return random integer in the range of the list
print random quote
"""
import random
quotes = [["Home is were the heart is"], ["Cut your coat according to ur size"], ["The boy cried wolf"], ["The lord is good"], ["Time is money"]]
index = random.randint(0, 4)
print(input(f"the random quotes is: {quotes[index]}"))
