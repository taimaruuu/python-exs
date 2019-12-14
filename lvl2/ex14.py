# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def remove_dup(lst):
    new_list = []
    for item in lst:
        if not item in new_list:
            new_list.append(item)
    return new_list

def remove_dup_set(lst):
    return list(set(lst))

def intersection(a, b):
    return list(set([num for num in a if num in b]))

a = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6]
print(remove_dup(a))
print(remove_dup_set(a))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(intersection(a,b))

