#Q.2 Write a Python program to solve the 8-Queen puzzle problem.

# Initialize an 8x8 board with 0's
N = 8
board = [[0 for _ in range(N)] for _ in range(N)]

# Function to check if placing a queen at board[row][col] is safe
def is_safe(board, row, col):
    # Check the row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Function to solve the 8-Queen puzzle using backtracking
def solve_queen(board, col):
    # If all queens are placed, return True
    if col >= N:
        return True

    # Place a queen in each row one by one
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queen(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack

    return False

# Function to print the board with queens placed
def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))

# Solve the 8-Queen puzzle and display the solution
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