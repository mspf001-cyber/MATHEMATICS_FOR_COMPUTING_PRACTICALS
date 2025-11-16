#!/usr/bin/env python3
"""
Practical 4
Solve a system Ax = b (non-homogeneous) using Gaussian elimination (with partial pivoting).
User provides augmented matrix rows (enter rows as 'a1 a2 ... an | b').
"""
import sys
import numpy as np

def read_augmented():
    print("Enter augmented matrix rows as: a1 a2 ... an | b  (blank line to use example):")
    Arows = []
    brows = []
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        if '|' in line:
            left, right = line.split('|',1)
        else:
            parts = line.split()
            left = " ".join(parts[:-1])
            right = parts[-1]
        a = [float(x) for x in left.split()]
        b = float(right.strip())
        Arows.append(a)
        brows.append(b)
    if not Arows:
        A = np.array([[2,1,-1],[ -3,-1,2],[ -2,1,2]], dtype=float)
        b = np.array([8, -11, -3], dtype=float)
        return A,b
    return np.array(Arows,dtype=float), np.array(brows,dtype=float)

def gauss_solve(A,b):
    A = A.copy().astype(float)
    b = b.copy().astype(float)
    n = A.shape[0]
    # forward elimination with partial pivoting
    for k in range(n):
        # pivot
        piv = np.argmax(np.abs(A[k:,k])) + k
        if abs(A[piv,k]) < 1e-12:
            continue
        if piv != k:
            A[[k,piv]] = A[[piv,k]]
            b[[k,piv]] = b[[piv,k]]
        for i in range(k+1,n):
            factor = A[i,k]/A[k,k]
            A[i,k:] -= factor*A[k,k:]
            b[i] -= factor*b[k]
    # back substitution
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        if abs(A[i,i]) < 1e-12:
            x[i] = 0.0
            continue
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:]))/A[i,i]
    return x

def main():
    A,b = read_augmented()
    print("A:\n",A)
    print("b:\n",b)
    try:
        x = gauss_solve(A,b)
        print("\nSolution x:\n", x)
    except Exception as e:
        print("Error solving:", e)

if __name__ == "__main__":
    main()
