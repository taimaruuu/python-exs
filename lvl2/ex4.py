# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = input("Please give a number to divide: ")
int_num = int(num)
range_list = list(range(1, int_num+1))

divisor_list = []

for x in range_list:
    if int_num % x == 0:
        divisor_list.append(x)

print( str(divisor_list) + " is the list of divisors of " + num)
