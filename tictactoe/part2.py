# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
# 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

winner_is_2 = [[2, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
    [2, 1, 0],
    [2, 1, 1]]

no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 2]]

also_no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 0]]

def check_line(board):
    # horizontal line win
    for row in board:
        if len(set(row)) == 1 and 0 not in row:
            if 1 in row:
                print("Player 1 is the winner")
            else:
                print("Player 2 is the winner")

    # vertical line win
    for i in range(0,3):
        col = list(set([board[0][i], board[1][i], board[2][i]]))
        if len(col) == 1 and 0 not in col:
            if 1 in col:
                print("Player 1 is the winner")
            else:
                print("Player 2 is the winner")

def check_diagonal(board):
    diags = [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[0][0]]
    for line in diags:
        if len(set(line)) == 1 and 0 not in line:
            if 1 in line:
                print("Player 1 is the winner")
            else:
                print("Player 2 is the winner")

def check_winner(board):
    check_line(board)
    check_diagonal(board)

check_winner(winner_is_2)
check_winner(winner_is_1)
check_winner(winner_is_also_1)
check_winner(no_winner)
check_winner(also_no_winner)
