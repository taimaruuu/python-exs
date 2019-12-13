# Alternate version where you play against the computer
# Make a one-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

import random

def compare(a, b):
    if (a == b):
        print("It's a tie")
    elif (a == "rock"):
        if (b == "paper"):
            print("User 1 wins. " + a.capitalize() + " beats " + b + ".")
        else:
            print("User 2 wins. " + b.capitalize() + " beats " + a + ".")
    elif (a == "paper"):
        if (b == "scissors"):
            print("User 1 wins. " + a.capitalize() + " beats " + b + ".")
        else:
            print("User 2 wins. " + b.capitalize() + " beats " + a + ".")
    elif (a == "scissors"):
        if (b == "rock"):
            print("User 1 wins. " + a.capitalize() + " beats " + b + ".")
        else:
            print("User 2 wins. " + b.capitalize() + " beats " + a + ".")
    else:
        print("Invalid input. At least one user didn't pick rock, paper, or scissors. Try again.")

print ("Welcome to Rock, Paper, Scissors!")

while True:
# get player 1 input
    input1 = input("Player 1 make a selection: ").lower()
 # get player 2 input
    computer_choice = random.randint(1, 3)
    choices = { 1: "rock", 2: "paper", 3: "scissors"}
    input2 = choices.get(computer_choice, "giberish")

# if one of the users wants to quit break the loop
    if input1 == "quit" or input2 == "quit":
        print("Bye, have a good day!")
        break

    compare(input1, input2)