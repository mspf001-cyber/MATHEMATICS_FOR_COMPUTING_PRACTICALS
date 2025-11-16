#!/usr/bin/env python3
"""
Practical 5
Solve homogeneous system Ax = 0 using Gauss-Jordan to find solution space (null space).
"""
import sys
import numpy as np

def read_matrix():
    print("Enter matrix A rows (space-separated). Blank -> example:")
    rows = []
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        rows.append([float(x) for x in line.split()])
    if not rows:
        return np.array([[1,2,-1, -1],[2,4,-2,-2],[1,0, 1, 0]], dtype=float)
    return np.array(rows,dtype=float)

def gauss_jordan(A):
    A = A.copy().astype(float)
    m,n = A.shape
    row = 0
    pivcols = []
    for col in range(n):
        if row >= m:
            break
        sel = np.argmax(np.abs(A[row:,col])) + row
        if abs(A[sel,col]) < 1e-12:
            continue
        A[[row,sel]] = A[[sel,row]]
        A[row] = A[row] / A[row,col]
        for r in range(m):
            if r != row:
                A[r] = A[r] - A[r,col]*A[row]
        pivcols.append(col)
        row += 1
    return A, pivcols

def null_space(A, tol=1e-10):
    # use SVD for numerical nullspace
    u,s,vt = np.linalg.svd(A)
    null_mask = (s <= tol)
    null_space = np.compress(null_mask, vt, axis=0)
    if null_space.size == 0:
        return np.zeros((A.shape[1],0))
    return null_space.T

def main():
    A = read_matrix()
    print("A:\n",A)
    GJ, piv = gauss_jordan(A)
    print("\nGauss-Jordan reduced form:\n", GJ)
    print("Pivot columns:", piv)
    ns = null_space(A)
    print("\nNull space basis (columns):\n", ns)
    if ns.size==0:
        print("Only trivial solution x=0 exists.")
    else:
        print("General solution is linear combination of these basis vectors.")

if __name__ == "__main__":
    main()
