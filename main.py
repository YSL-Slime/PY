import random

COLS = 3
ROWS = 5
LINES_MAX = 3
BET_MIN = 1
BET_MAX = 100

colors = {'R', 'B', 'G', '7', 'C', 'X', 'T'}

vals = {
    'R' : 2 ** 3, 
    'B' : 3 ** 2,
    'G' : 3 ** 3,
    '7' : 7 ** 3, 
    'C' : 2,
    'X' : 3, 
    'T' : 2 ** 2
}

def winning(r, bet, lines, vals):
    won = 0
    wl = []
    for line in range(lines):
        s = r[0][line]
        for c in r:
            sc = c[line]
            if s != sc:
              break
        else:
            won += vals[s] * bet
            wl.append(line + 1)
    return won, wl
          
def spin(r, c, colors):
    sy = []
    for s in colors:
        sy.append(s)
    row = []
    for _ in range(c):
        column = []
        csy = sy[:]
        for _ in range(r):
            v = random.choice(csy)
            column.append(v)
            csy.remove(v)
        row.append(column)
    
    return row

def display(r):
    print("---------")
    for p in range(len(r[0])):
        for i, c in enumerate(r):
            if i != len(r) - 1:
                print(c[p], end=" | ")
            else:
                    print(c[p], end="")
        print()
    print("---------")

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
game = True
while game:
    balance -= bets * lines
    print(f"The bet is {bets} for {lines} lines. Total bet: {bets * lines}")
    tt = spin(ROWS, COLS, colors)
    display(tt)
    won, onl = winning(tt, bets, lines, vals)
    print(f"You won ${won} for line/s", *onl)
    
    again = input("Do you want to: Play again (Enter), Add to your balance (a), Change lins (l), Change bet(b), or Quit (q)")
    
    match again:
        case '':
            continue
        case 'a':
            balance += deposit()
        case 'l':
            lines = betingLines()
        case 'b':
            while True:
                bets = bet()
                if bets * lines > balance:
                    print(f"Not enough facilities for the bet. Balance: {balance}")
                else:
                    break
        case 'q':
            game = False
            