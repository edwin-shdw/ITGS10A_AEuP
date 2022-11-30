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
                invalid = player.bet < MIN_BET or player.bet > MAX_BET
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
        action = input("Your action? Hit(H) / Stand(S) / Double(D) ")
        if action == 'H': player.hit(takeCard(play_deck))
        elif action == 'D': 
            player.setBet(player.bet*2)
            player.hit(takeCard(play_deck))
            break
        else: break
        player.checkAce()
        if player.checkBust():
            print(f"{player.name} lost. ({player.getCardsSum()})")
            player.busted()

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
        deck = creatBlackJackDeck() * CARD_DECKS_USED
        input("RESHUFFLED")


# ---------- MAIN ----------
play_deck = creatBlackJackDeck() * CARD_DECKS_USED
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
        
    print(f"Dealers Cards: {dealer.getCardDeck()} = {dealer.getCardsSum()}")
    for player in players:
        print(f"{player.name}'s Cards: {player.getCardDeck()} = {player.getCardsSum()}")
        print(f"{player.name}'s cap: {player.capital}")
    
    next_round = (input("Next round? (Y / N) ") == 'Y')

# TODO: add action split
