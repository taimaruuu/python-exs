# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

num_2_guess = random.randint(1, 9)
count = 0

while True:
    user_guess = input("Guess a number between 1-9: ").lower()
    count += 1

    if user_guess == "exit": 
        print("Goodbye, you made " + str(count) + " guesses.")
        break
    elif int(user_guess) == num_2_guess:
        print("Good job, you guessed the right number in " + str(count) + " tries.")
        break
    elif int(user_guess) > num_2_guess:
        print("You guessed too high, guess again")
    else:
        print("You guessed too low, guess again")
