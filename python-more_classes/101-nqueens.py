#!/usr/bin/python3
"""Solves the N queens puzzle and prints every solution."""
import sys


def solve(n, row, cols, solution, results):
    """Place queens row by row using backtracking."""
    if row == n:
        results.append([[r, c] for r, c in enumerate(solution)])
        return
    for col in range(n):
        safe = True
        for r in range(row):
            c = solution[r]
            if c == col or abs(c - col) == row - r:
                safe = False
                break
        if safe:
            solution.append(col)
            solve(n, row + 1, cols, solution, results)
            solution.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    results = []
    solve(n, 0, None, [], results)
    for result in results:
        print(result)
