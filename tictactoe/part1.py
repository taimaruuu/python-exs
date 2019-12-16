# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

def print_horiz_line():
    print(" ---" * size)

def print_vert_line():
    print("|   " * (size + 1))

def print_board():
    print_horiz_line()
    for i in range(size):
        print_vert_line()
        print_horiz_line()

if __name__ == "__main__":
    size = int(input("What size of game board? "))
    print_board()