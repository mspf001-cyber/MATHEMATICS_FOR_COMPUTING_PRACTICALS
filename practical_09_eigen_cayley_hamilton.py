#!/usr/bin/env python3
"""
Practical 9
Check diagonalizability, compute eigenvalues/eigenvectors, verify Cayley-Hamilton theorem.
Uses numpy for numeric eigen decomposition and sympy for symbolic Cayley-Hamilton verification.
"""
import sys
import numpy as np
from sympy import Matrix

def read_square_matrix():
    print("Enter square matrix rows (space-separated). Blank -> default 3x3:")
    rows=[]
    while True:
        l=sys.stdin.readline().strip()
        if l=="":
            break
        rows.append([float(x) for x in l.split()])
    if not rows:
        return np.array([[5,-2,2],[-1,3,0],[0,0,4]], dtype=float)
    M = np.array(rows,dtype=float)
    if M.shape[0]!=M.shape[1]:
        raise SystemExit("Matrix must be square.")
    return M

def is_diagonalizable(A):
    vals, vecs = np.linalg.eig(A)
    rank_vecs = np.linalg.matrix_rank(vecs)
    return rank_vecs == A.shape[0], vals, vecs

def main():
    A = read_square_matrix()
    print("A:\n",A)
    diag, vals, vecs = is_diagonalizable(A)
    print("\nEigenvalues (numeric):\n", vals)
    print("\nEigenvectors (columns):\n", vecs)
    print("\nDiagonalizable?:", diag)
    # Cayley-Hamilton via sympy
    symA = Matrix(A)
    charpoly = symA.charpoly()
    cp = charpoly.as_expr()
    print("\nCharacteristic polynomial (sympy):", cp)
    # evaluate polynomial at matrix
    P = symA.as_explicit_matrix().subs if False else None
    # directly use sympy to evaluate polynomial: symA.charpoly().as_expr()(symA) isn't direct; use .eval
    try:
        from sympy import simplify
        x = sympy_symbol = charpoly.gen
        poly = cp
        # substitute matrix into polynomial: use sympy Polynomial matrix eval
        res = poly.subs({x: symA})  # works in sympy: polynomial of matrix
        print("\nCayley-Hamilton evaluation (should be zero matrix):\n", simplify(res))
    except Exception:
        # fallback numeric check: compute coefficients and evaluate
        coeffs = symA.charpoly().all_coeffs()
        # evaluate p(A) = a0*A^n + a1*A^(n-1) + ... + an*I
        n = A.shape[0]
        # convert sympy coeffs to floats
        coeffs_f = [float(c) for c in coeffs]
        A_pow = np.eye(n)
        res_num = np.zeros_like(A, dtype=float)
        for i,coeff in enumerate(coeffs_f):
            power = n - i
            res_num += coeff * np.linalg.matrix_power(A, power-1) if power-1 >=0 else coeff * np.eye(n)
        print("\nNumeric Cayley-Hamilton check (approx):\n", res_num)

if __name__ == "__main__":
    main()
