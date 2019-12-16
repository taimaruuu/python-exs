# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

#     Use binary search.

def binary_search(num_list, start, end, key):

    if start >= end:
        return False

    mid = (start + end) // 2

    if num_list[mid] < key:
        return binary_search(num_list, mid + 1, end, key)
    elif num_list[mid] > key:
        return binary_search(num_list, start, mid, key)
    else:
        return True

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 7]
    answer = binary_search(a, 0, len(a), 10)
    print(answer)

    a = [1, 2]
    answer = binary_search(a, 0, len(a), 2)
    print(answer)

    a = []
    answer = binary_search(a, 0, len(a), 10)
    print(answer)