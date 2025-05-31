import random


print("Welcome to the Dice Roller!")
players = int(input("How many players are playing :"))

for player in range(1, players + 1):
    roll = random.randint(1, 6)
    print(f"Dice rolled for player{player} : {roll}")