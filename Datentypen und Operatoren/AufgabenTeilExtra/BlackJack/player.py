class Player:
    def __init__(self, name, bet, capital = 1000):
        self.name = name
        self.cards = []
        self.currentBet = bet
        self.capital = capital

    def hit(self, card):
        self.cards.append(card)

    def getCardsSum(self):
        sum = 0
        for card in self.cards:
            sum += card.value
        return sum

    def getCardDeck(self, fCards=0):
        arr = []
        fCards = len(self.cards) - fCards
        for i, card in enumerate(self.cards):
            if i >= fCards:
                arr.append('\u2610')
            else: arr.append(card.getCard())
        return(arr)

    def setBet(self, bet):
        self.currentBet = bet

    def lostBet(self):
        self.capital -= self.currentBet

    def wonBet(self):
        self.capital += self.currentBet

class BlackJackPlayer(Player):
    def __init__(self, name, bet=0, capital = 1000):
        Player.__init__(self, name, bet, capital)
        self.bust = False
        self.blackJack = False

    def checkBlackJack(self):
        self.blackJack = (self.getCardsSum() == 21)
        return self.blackJack

    def checkBust(self):
        self.bust = (self.getCardsSum() > 21)
        return self.bust

    def busted(self):
        self.bust = True

    def checkAce(self):
        for card in self.cards:
            if card.index == 'A' and self.getCardsSum() > 21:
                card.value = 1

    def resetCards(self):
        self.cards = []
        self.bust = False
        self.blackJack = False
        