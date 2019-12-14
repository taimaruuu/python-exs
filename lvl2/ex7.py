# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
import random 

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = random.sample(range(0, 100), random.randint(0, 25))
even_a = []
even_b = []

# expanded solution for a and b
for item in a:
    if item % 2 == 0:
        even_a.append(item)

for item in b:
    if item % 2 == 0:
        even_b.append(item)

print(even_a)
print(even_b)

even_a = []
even_b = []
# one line solution for a and b
even_a = [x for x in a if x % 2 == 0]
even_b = [x for x in b if x % 2 == 0]

print(even_a)
print(even_b)