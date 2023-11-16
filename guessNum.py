import random
import math

min = int(input("What is the minimum number: "))
max = int(input("What is the maximum number: "))



i = int((min + max) / 2)
print(f"You have {i} guesses!")
j = 0
num = random.randint(min, max)

while(j < i):
        a = input("Guess: ")

        if int(a) == num:
            print("CORRECT!")
            break
        elif int(a) < num:
            print("TOO LOW!")
            j += 1
        else:
            print("TOO HIGH!")
            j += 1