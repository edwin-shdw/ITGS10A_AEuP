import random

GREEN_NUMBER = 0
RED_NUMBERS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
BLACK_NUMBERS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
START_CAPITAL = 200
MIN_BET = 2
MAX_BET = 100

SIM_C = 1000

total_loss_count = 0
avg_win_capital = 0

def simulateRound(col, bet):
    global current_capital
    if bet >= current_capital: bet = current_capital
    elif bet >= MAX_BET: bet = MAX_BET
    round_won = isWin(col)
    if round_won:
        current_capital += bet
    else: current_capital -= bet
    return round_won

def simulateVisit():
    current_bet = MIN_BET
    for i in range(500):
        prev_round_won = simulateRound(color, current_bet)
        if current_capital <= 0:
            #print(f"DAS SPIEL IST NACH {i+1} RUNDEN VORBEI")
            break
        if prev_round_won: current_bet = MIN_BET
        else: current_bet *= 2
    #print(f"DIE SIMULATION IST ZU ENDE UND ES WURDE EIN GEWINN/VERLUST VON {current_capital - START_CAPITAL} GEMACHT")
    return current_capital

def isWin(color):
    ball_on = random.randrange(0, 36)
    return (ball_on in RED_NUMBERS and color == "red") or (ball_on in BLACK_NUMBERS and color == "black")

while True:
    color = (input("Auf welche Farbe setzen Sie? (red / black) ")).lower()
    if color == "red" or color == "black":
        for i in range(SIM_C):
            current_capital = START_CAPITAL
            current_capital = simulateVisit()
            if not current_capital: total_loss_count += 1
            avg_win_capital += current_capital - START_CAPITAL
        print(f"Totaler Verlust in {(total_loss_count / SIM_C * 100):.2f} % der Fälle")
        print(f"Durchcshnittliche Gewinn/Verlust: {avg_win_capital / SIM_C}")
        break
    else: print("Das ist keine gegebene Auswahlmöglichkeit!")
