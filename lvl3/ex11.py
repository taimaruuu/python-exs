# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

def divisor_list(num):
    div_range = range(1, num+1)
    div_list = [item for item in div_range if num % item == 0]
    return div_list

num = int(input("Give me a number and I will tell you if its prime or not: "))
div_list = divisor_list(num)
if len(div_list) == 2 and 1 in div_list and num in div_list:
    print("The number you chose (" + str(num) + ") is prime.")
else:
    print("The number you chose (" + str(num) + ") is not prime.")


