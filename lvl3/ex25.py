# You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

def binary_search(nums, start, end, count):
    count += 1
    if start >= end:
        print("The number you gave is not between 0 and 100")
        return

    mid = (start + end) // 2
    key = int(input("Is your number " + str(nums[mid]) + "? (1 means too low, 2 means too high, 0 means the right number) "))

    # -1 means too low
    if key == 1:
        return binary_search(nums, mid + 1, end, count)
    # 1 means too high
    elif key == 2:
        return binary_search(nums, start, mid, count)
    elif key == 0:
        print("We found your guess in " + str(count) + " tries")
        return

if __name__ == "__main__":
    print("Think of a number in your head")

    binary_search(range(0, 100), 0, 100, 0)

