import random

score_player = 0
score_pc = 0

while True:
    while True:
        roll = random.randint(1, 6)
        print(f"You rolled {roll}")
        if roll == 1:
            score_player = 0
            break
        else:
            score_player += roll
        print(f"You have {score_player} points. PC has {score_pc} points.")
        print("Roll again?")
        a = input("Enter or N:  ")
        match a:
            case '':
                continue
            case 'N':
                break
    
    while True:
        roll = random.randint(1, 6)
        print(f"PC rolled {roll}")
        if roll == 1:
            score_pc = 0
            break
        else:
            score_pc += roll
        if score_pc > 15:
            xx = random.randint(1, 2)
            if xx == 2:
                continue
            else:
                break
    
    if score_player >= 100:
        print(f"You won with {score_player} points!")
    if score_pc >= 100:
        print(f"PC won with {score_pc} points!")  