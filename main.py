import random
COLS = 6
ROWS = 7
LINES_MAX = 3
BET_MIN = 1
BET_MAX = 100

colors = {'R', 'B', 'G', '7', 'C', 'X', 'T'}

def spin(r, c, colors):
    display = []
    for _ in range(r):
        column = []
        for _ in range(c):
            column.append('X')
        display.append(column)
    print(display)

def deposit():
    while True:
        amount = input("How much: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Muse be more then 0")
        else:
            print("Enter a number!")
    return amount
                
def betingLines():
    while True:
            lines = input(f"How many lines to bet on (1 - {LINES_MAX})? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= LINES_MAX:
                    break
                else:
                    print("Enter a valid number of lines!")
            else:
                print("Enter a number!")
    return lines

def bet():
    while True:
        amount = input("How much will you bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if BET_MIN <= amount <= BET_MAX:
                break
            else:
                print(f"Muse be between {BET_MIN} and {BET_MAX}!")
        else:
            print("Enter a number!")
    return amount
            
balance = deposit()
lines = betingLines()

while True:
    bets = bet()
    if bets * lines > balance:
        print(f"Not enough facilities for the bet. Balance: {balance}")
    else:
        break
    
print(f"The bet is {bets} for {lines} lines. Total bet: {bets * lines}")
spin(ROWS, COLS, colors)