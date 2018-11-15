import random

#List that has the card values from 2 to Ace
c_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

#List that has all different suits (Hearts, Diamonds, Spades and Clubs)
colors = ['H', 'D', 'S', 'C']

#Class for creating card objects
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __str__(self):
        return "%s%s" % (self.color, self.value)


#Create a deck of cards from card objects
deck = [Card(value, color) for value in c_values for color in colors]

#Hands for player 1 and 2
hand1 = []
hand2 = []


#Function to shuffle the deck
def shuffle():
    random.shuffle(deck)


#Function to deal first hands from the deck
def deal_hands():

    i=0
    while i <= 5:
        hand1.append(deck.pop())
        hand2.append(deck.pop())
        i += 1


#Function to print hands players currently have
def print_hands():
    temp_str = ""
    for i in hand1:
        temp_str = temp_str+"["+str(i)+"]"+" "
    print("Player 1's hand:\n" + temp_str + "\n")

    temp_str = ""
    for i in hand2:
        temp_str = temp_str+"["+str(i)+"]"+" "
    print("Player 2's hand:\n" + temp_str + "\n")


def main():
    shuffle()
    deal_hands()
    print_hands()



if __name__ == '__main__':
    main()





