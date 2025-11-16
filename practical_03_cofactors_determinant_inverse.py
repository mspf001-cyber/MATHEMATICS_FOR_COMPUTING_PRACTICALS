#!/usr/bin/env python3
"""
Practical 3
Compute cofactors, determinant, adjoint (adjugate) and inverse.
Uses numpy and sympy for cofactors/adjoint (symbolic if needed).
"""
import numpy as np
import sys
from sympy import Matrix

def read_square_matrix():
    print("Enter square matrix rows (space-separated). Blank line to finish (empty -> default 3x3):")
    rows = []
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        rows.append([float(x) for x in line.split()])
    if not rows:
        return np.array([[1,2,3],[0,4,5],[1,0,6]], dtype=float)
    A = np.array(rows, dtype=float)
    if A.shape[0] != A.shape[1]:
        raise SystemExit("Matrix must be square.")
    return A

def main():
    A = read_square_matrix()
    print("Matrix A:\n", A)
    det = np.linalg.det(A)
    print("\nDeterminant (numeric):", det)
    # use sympy for cofactors and adjugate
    M = Matrix(A)
    adj = M.adjugate()
    cofactors = M.cofactor_matrix()
    print("\nCofactor matrix (sympy):\n", cofactors)
    print("\nAdjugate (adjoint) matrix (sympy):\n", adj)
    if abs(det) < 1e-12:
        print("\nMatrix is singular; inverse does not exist.")
    else:
        inv = np.linalg.inv(A)
        print("\nInverse (numpy):\n", inv)

if __name__ == "__main__":
    main()
