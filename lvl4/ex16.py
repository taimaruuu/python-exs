# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

#     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import string
import random

def gen_pass(strenght):
    s = string.printable
    whitespace = string.whitespace
    characters = [char for char in s if char not in whitespace]
    strength_dict = {"weak": 4, "medium": 8, "strong": 12}
    return ''.join(random.sample(characters, strength_dict.get(strenght)))

def main():
    strength = input("Please give me a password strength you'd like (weak, medium, strong): ")
    print("Here is your password: " + gen_pass(strength))

if __name__ == '__main__':
    main()