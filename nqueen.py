# N Queens Problem

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):

    # Check left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Upper diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Lower diagonal
    i = row
    j = col

    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nq(board, col, n):

    if col >= n:
        return True

    for i in range(n):

        if is_safe(board, i, col, n):

            board[i][col] = 'Q'

            if solve_nq(board, col + 1, n):
                return True

            board[i][col] = '.'

    return False


n = int(input("Enter value of N: "))

board = [['.' for x in range(n)] for y in range(n)]

if solve_nq(board, 0, n):
    print("\nSolution:")
    print_board(board, n)
else:
    print("No solution exists")
