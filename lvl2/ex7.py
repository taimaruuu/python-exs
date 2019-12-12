# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
random_a = random.sample(range(0, 100), random.randint(0, 25))
even = []

# expanded solution for a and random_a
for item in a:
    print(item)
    even.append(item if item % 2 == 0)

print(even)


# one line solution for a and random_a

