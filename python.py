import random
import math
#stack = []
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#colours = ['Red', 'Blue', 'Yellow', 'Green']
#superCards = ['Skip', 'Wild Card', '+2', 'Reverse']

def deckOfCards():
    stack = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    colours = ['Red', 'Blue', 'Yellow', 'Green']
    superCards = ['Skip', 'Wild Card', '+2', 'Reverse']

    for colour in colours:
        for number in numbers:
            cards = '{} {}'.format(colour, number)
            stack.append(cards)
        for superCard in superCards:
            cards = '{} {}'.format(colour, superCard)
            stack.append(cards)
    print(stack)
    return(stack)
deckOfCards()

