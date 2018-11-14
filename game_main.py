import random

#Class for creating card objects
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __str__(self):
        return "%s:%s" % (self.color, self.value)

#Global variables
colors = ['H', 'D', 'S', 'C']

#Create a deck of cards from card objects
deck = [Card(value, color) for value in range (1, 15) for color in colors]

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





