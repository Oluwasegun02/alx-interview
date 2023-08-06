#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard
"""

import sys

def is_safe(board, row, col):
    """ Check if a queen can be placed at the given position"""
  
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def nqueens(board, row, N):
    """ Base case: All queens are placed"""
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
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
    global solutions
    solutions = []
    nqueens(board, 0, N)

    for solution in solutions:
        print(solution)

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
