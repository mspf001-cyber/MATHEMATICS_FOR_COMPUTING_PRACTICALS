Practical 2
Generate row-echelon form and compute rank.
Uses numpy and a simple row-reduction routine for echelon form.
"""
import numpy as np
import sys

def read_matrix():
    print("Enter matrix rows (space-separated). Blank line to finish (empty -> default):")
    rows = []
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        rows.append([float(x) for x in line.split()])
    if not rows:
        return np.array([[1,2,3],[2,4,6],[1,1,0]], dtype=float)
    return np.array(rows, dtype=float)

def row_echelon(A):
    A = A.astype(float).copy()
    m, n = A.shape
    r = 0
    for c in range(n):
        # find pivot
        piv = None
        for i in range(r, m):
            if abs(A[i,c]) > 1e-12:
                piv = i
                break
        if piv is None:
            continue
        if piv != r:
            A[[r,piv]] = A[[piv,r]]
        A[r] = A[r] / A[r,c]
        for i in range(r+1, m):
            A[i] = A[i] - A[i,c]*A[r]
        r += 1
        if r == m:
            break
    return A

def main():
    A = read_matrix()
    print("Original matrix:\n", A)
    E = row_echelon(A)
    print("\nRow echelon form:\n", E)
    # rank via numpy
    rank = np.linalg.matrix_rank(A)
    print("\nRank (numpy.linalg.matrix_rank):", rank)

if __name__ == "__main__":
    main()
