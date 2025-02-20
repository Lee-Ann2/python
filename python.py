import random
import math
from os import remove

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

def drawingCards():
    cardsToDraw = []
    numCards = 0
    for x in range(numCards):
        cardsToDraw.append(deckOfCards)

num_of_players = []
players = input('enter number of players')
for num_of_players in range(players):
    num_of_players.append(drawingCards(8))
    
#Enter the condition in here

def options(player, playersOptions):
    print('player {}'.format(player))
    for cards in playersOptions:
        print(cards)
    print(cards)

turn = 0
direction = 0
playing =True

while playing:
    options(turn, num_of_players[turn])
    print('pile: {}'.format(remove[-1]))
