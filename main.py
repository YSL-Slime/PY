from SlotMachine import SlotMachine
import tkinter as tk
from tkinter import messagebox

COLS = 3
ROWS = 5

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

def game():      
    balance = SlotMachine.deposit()
    lines = SlotMachine.betingLines()
    while True:
        bets = SlotMachine.bet()
        if bets * lines > balance:
            print(f"Not enough facilities for the bet. Balance: {balance}")
        else:
            break
    game = True
    while game:
        balance -= bets * lines
        print(balance)
        print(f"The bet is {bets} for {lines} lines. Total bet: {bets * lines}")
        tt = SlotMachine.spin(ROWS, COLS, colors)
        SlotMachine.display(tt)
        won, onl = SlotMachine.winning(tt, bets, lines, vals)
        print(f"You won ${won} for line/s", *onl)
        balance += won
        again = input("Do you want to: Play again (Enter), Add to your balance (a), Change lins (l), Change bet(b), or Quit (q)")
        
        match again:
            case '':
                while bets * lines > balance:
                    print(f"Not enough facilities for the bet. Balance: {balance}")
                    balance += SlotMachine.deposit()
                continue
            case 'a':
                balance += SlotMachine.deposit()
            case 'l':
                lines = SlotMachine.betingLines()
            case 'b':
                while True:
                    bets = SlotMachine.bet()
                    if bets * lines > balance:
                        print(f"Not enough facilities for the bet. Balance: {balance}")
                    else:
                        break
            case 'q':
                game = False
                
game()