# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = input("Please give me a number to check: ")
divisor = input("Please give me a number to divide by: ")
print("The number you gave is " + num + ".")


if int(num) % 4 == 0:
	print("This number is an even number and a multiple of 4.")
elif int(num) % 2 == 0:
	print("This number is an even number")
else:
	print("This number is not even nor a multiple of 4")

if int(num) % int(divisor) == 0:
	print(num + " divides evenly by" + divisor)
else: 
	print(num + " doesn't divide evenly by " + divisor)

