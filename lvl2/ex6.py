# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = input("Please give me a word to check to see if its a palindrome: ")
reverse_word = word[::-1]

if word == reverse_word:
    print("Your word (" + word + ") is a palindrome")
else:
    print("Your word (" + word + ") is not a palindrome")
