# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random #to provide random numbers
# random.randint(start, end) gives a random number between the range

limit = 100
size_limit = 25

# one way of getting a random list
random_a = random.sample(range(0, limit), random.randint(0, size_limit))

# a second way of getting a random list
random_b = [random.randint(0, 100) for num in range(size_limit)]

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# print (str(len(a)) + "vs" + str(len(b)) + "=" + str(bigger_list_size))
print("Random list 'a' is: " + str(random_a))
print("Random list 'b' is: " + str(random_b))

for item in random_a:
    if (item in random_b) and not (item in c):
        c.append(item)

print(str(c) + " is a list of items in both lists.")