# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:

#     Ask the user to specify the name of the output file that will be saved.


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
    file = input("Please give me a file to write to: ")
    openfile = open(file, 'a')
    openfile.write("Here is your password with strength (" + strength + "): " + gen_pass(strength))
    openfile.close()

if __name__ == '__main__':
    main()