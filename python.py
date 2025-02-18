import random
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
colours = ['Red', 'Blue', 'Yellow', 'Green']
superCards = ('Skip', 'Wild Card', 2, 'Reverse')

def deckOfCards():
    for number in numbers:
        for colour in colours:
            print(colour, end=' ')
    number += 1