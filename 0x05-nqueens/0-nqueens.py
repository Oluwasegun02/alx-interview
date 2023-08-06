#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard
"""

import sys

def is_safe(board, row, column):
    """Check if a qeen can be placed at the given position"""
    for i in range(row):
        if board[i] == column or abs(board[i] - column) == abs(i - row):
            return False
    return True
def nqueens(board, row, N):
    """Base case: All queens are place"""
    if row == N:
        print([i for i in board])
        return

    for column in range(N):
        if is_safe(board, row, column):
            board[row] = column
            nqueens(board, row + 1, N)
            board[row] = -1

def solve_nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

