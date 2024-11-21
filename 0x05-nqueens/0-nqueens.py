#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col)."""
    for i in range(row):
        # Check column and diagonals
        if board[i][1] == col or \
           board[i][1] - i == col - row or \
           board[i][1] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    """Solve the N-Queens problem using backtracking."""
    if row == N:
        # Found a valid solution, print it
        print(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(board, row + 1, N)
            board.pop()


def nqueens(N):
    """Solve the N-Queens problem for a given N."""
    board = []
    solve_nqueens(board, 0, N)


def main():
    """Main function to handle user input and validate."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)

if __name__ == "__main__":
    main()
