"""
Deal a hand of 5 cards
"""
import random

suits = ['♠︎', '♣︎', '♥︎', '♦︎']
rankes = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cards = []
for suit in suits:
    for rank in rankes:
        cards.append(suit+rank)
print(cards)
print(len(cards))

hand = []
for i in range(5):
    card=random.choice(cards)
    hand.append(card)



print(hand)
