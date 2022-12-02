from cards import *
from player import *
import os

MIN_PLAYER_AMOUNT = 1
MAX_PLAYER_AMOUNT = 5
MIN_BET = 5
MAX_BET = 100
BET = 50
CARD_DECKS_USED = 6

def newGame():
    dealer.resetCards()
    for player in players:
        player.resetCards()

def setBets():
    for player in players:
        invalid = True
        while invalid:
            try:
                player.setBet(int(input(f"{player.name} set your bet: ")))
                invalid = player.currentBet < MIN_BET or player.currentBet > MAX_BET
            except: invalid = True

def handOutCards():
    for i in range(2):
        dealer.hit(takeCard(play_deck))
        for player in players:
            player.hit(takeCard(play_deck))

def playerTurn(player):
    while not player.bust and not player.blackJack:
        if player.checkBlackJack():
            print("Black Jack!")
            break
        print(f"{player.name}'s Cards: {player.getCardDeck()} = {player.getCardsSum()}")
        action = input("Your action? Hit(H)  / Stand(S) / Double(D) / Split(Sp)) ")
        if action == 'H': player.hit(takeCard(play_deck))
        elif action == 'D': 
            player.setBet(player.currentBet*2)
            player.hit(takeCard(play_deck))
            break
        elif action == 'Sp':
            if len(player.cards) == 2 and player.cards[0].index == player.cards[1].index:
                playerSplits(player)
            else: print("Can't split your current deck")
        else: break
        player.checkAce()
        if player.checkBust():
            print(f"{player.name} lost. ({player.getCardsSum()})")
            player.busted()

def playerSplits(player):
    list_index = getIndex(players, player)+1
    players.insert(list_index, BlackJackPlayer(f'{player.name}Split', player.currentBet, 0))
    players[list_index].hit(player.cards[1])
    splits.append(players[list_index])
    player.cards.remove(player.cards[1])

def mergeSplits(players, splits):
    for split in splits:
        for player in players:
            if split.name == f"{player.name}Split":
                player.capital += split.capital
                if split in players: players.remove(split)

def clearSplits():
    for split in splits:
        if split in splits: splits.remove(split)

def dealerTurn(dealer):
    while dealer.getCardsSum() < 17:
        dealer.hit(takeCard(play_deck))
    dealer.checkBust()

def checkWin(dealer, player):
    if player.bust or (dealer.getCardsSum() > player.getCardsSum() and not dealer.checkBust()) or dealer.checkBlackJack():
        player.lostBet()
    elif dealer.getCardsSum() < player.getCardsSum() or (dealer.bust and not player.bust):
        player.wonBet()

def checkDeck(deck):
    if len(deck) <= (len(players) + 1) * 5:
        deck = createBlackJackDeck() * CARD_DECKS_USED

def getIndex(list, element):
    for i in range(len(list)):
        if element == list[i]:
            return i


# ---------- MAIN ----------
play_deck = createBlackJackDeck() * CARD_DECKS_USED
splits = []
dealer = BlackJackPlayer('Dealer')
players = []
player_amount = int(input(f"Amount of player ({MIN_PLAYER_AMOUNT} - {MAX_PLAYER_AMOUNT}): "))
if player_amount >= MIN_PLAYER_AMOUNT and player_amount <= MAX_PLAYER_AMOUNT:
    for i in range(player_amount):
        players.append(BlackJackPlayer(f'Player{i+1}'))
else: print("Invalid lul")

next_round = True
while next_round:
    checkDeck(play_deck)
    newGame()
    setBets()
    handOutCards()
    if not dealer.checkBlackJack():
        for player in players:
            os.system('clear')
            print(f"{dealer.name}'s Cards: {dealer.getCardDeck(1)}")
            playerTurn(player)
        dealerTurn(dealer)
        for player in players:
            checkWin(dealer, player)
    else:
        print("Dealer wins")
        for player in players:
            player.lostBet()
        
    mergeSplits(players, splits)

    print(f"Dealers Cards: {dealer.getCardDeck()} = {dealer.getCardsSum()}")
    for i, player in enumerate(players):
        print(f"{player.name}'s Cards: {player.getCardDeck()} = {player.getCardsSum()}")
        for split in splits:
            if f'{player.name}Split' == split.name:
                print(f"{split.name}'s Cards: {split.getCardDeck()} = {split.getCardsSum()}")
        print(f"{player.name}'s cap: {player.capital}\n")
    clearSplits()
    
    next_round = (input("Next round? (Y / N) ") == 'Y')

# TODO: feat-test splitting
