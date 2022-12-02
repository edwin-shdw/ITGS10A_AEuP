import random

CARD_INDEXES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_ICONS = ['\u2660', '\u2665', '\u2666', '\u2663'] # [spades, heart, diamond, clubs]

class Card:
    def __init__(self, icon, index):
        self.icon = icon
        self.index = index

    def getCard(self):
        return f"{self.icon}{self.index}"

class BlackJackCard(Card):
    def __init__(self, icon, index):
        Card.__init__(self, icon, index)
        self.value = self.setValue()

    def setValue(self):
        try:
            return int(self.index)
        except:
            if self.index == 'J' or self.index == 'Q' or self.index == 'K':
                return 10
            elif self.index == 'A':
                return 11

def takeCard(deck):
    rand_card = deck[random.randrange(0, len(deck))]
    deck.remove(rand_card)
    return rand_card

def createBlackJackDeck():
    deck = []
    for icon in CARD_ICONS:
        for index in CARD_INDEXES:
            deck.append(BlackJackCard(icon, index))
    return deck


# ========== for development ==========
def createTestDeck():
    deck = []
    for icon in CARD_ICONS:
        for index in CARD_INDEXES[7:9]:
            deck.append(BlackJackCard(icon, index))
    return deck
    