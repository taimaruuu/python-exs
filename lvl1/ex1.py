# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
import datetime

name = input("What is your name? ")
name = name.capitalize()
age = input ("What is your age? ")
rep = input("Give me a number: ")
now = datetime.datetime.now()
year_when_100 = now.year - int(age) + 100

for x in range(int(rep)):
	print("Hello " + name + ", you will be 100 years old in " + str(year_when_100))
