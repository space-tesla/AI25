#Q.2 Write a Python program to solve the 8-Queen puzzle problem.

N = 8
board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queen(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queen(board, col + 1):
                return True
            board[i][col] = 0  

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))

if solve_queen(board, 0):
    print("One possible solution to the 8-Queen puzzle:")
    print_board(board)
else:
    print("No solution found.")




"""Output:

One possible solution to the 8-Queen puzzle:
Q . . . . . . .
. . . . Q . . .
. . . . . . Q .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . Q . . . . ."""