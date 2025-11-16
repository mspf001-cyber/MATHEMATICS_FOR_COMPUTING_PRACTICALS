#!/usr/bin/env python3
"""
Practical 6
Generate basis of column space, null space, row space and left null space.
Also compute transition matrix between two bases if provided.
"""
import sys
import numpy as np

def read_matrix(prompt="Enter matrix rows (space-separated). Blank -> default:"):
    print(prompt)
    rows=[]
    while True:
        line=sys.stdin.readline().strip()
        if line=="":
            break
        rows.append([float(x) for x in line.split()])
    if not rows:
        return np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)
    return np.array(rows,dtype=float)

def column_space_basis(A):
    # columns corresponding to pivot columns of RREF
    u,s,vt = np.linalg.svd(A)
    rank = np.linalg.matrix_rank(A)
    return A[:, :rank] if rank>0 else np.zeros((A.shape[0],0))

def null_space_basis(A):
    u,s,vt = np.linalg.svd(A)
    rank = np.linalg.matrix_rank(A)
    return vt.T[:, rank:]

def row_space_basis(A):
    return A[:np.linalg.matrix_rank(A), :]

def left_null_space_basis(A):
    # null space of A^T
    return null_space_basis(A.T)

def transition_matrix(B_from, B_to):
    # Both are arrays whose columns are basis vectors; compute P such that [id]_to = P [id]_from
    # Solve B_to = B_from * P  => P = B_from^{-1} B_to (if B_from square/invertible) or solve least squares
    # We compute coefficients of B_to expressed in B_from
    # Use numpy.linalg.lstsq
    P, *_ = np.linalg.lstsq(B_from, B_to, rcond=None)
    return P

def main():
    A = read_matrix("Enter matrix A rows (space-separated). Blank -> default:")
    print("A:\n",A)
    rank = np.linalg.matrix_rank(A)
    print("Rank:", rank)
    # Column space basis (via SVD approximation)
    U, s, Vt = np.linalg.svd(A)
    col_basis = A[:, :rank] if rank>0 else np.zeros((A.shape[0],0))
    null_basis = null_space_basis(A)
    left_null = left_null_space_basis(A)
    print("\nColumn space basis (approx):\n", col_basis)
    print("\nNull space basis (columns):\n", null_basis)
    print("\nLeft null space basis (columns):\n", left_null)
    # Transition matrix demo: ask user for two bases with same dimension
    print("\nOPTIONAL: Enter two bases (each column vector per line, components space-separated). Blank to skip.")
    print("First basis (enter k lines for k columns):")
    lines=[]
    while True:
        l=sys.stdin.readline().strip()
        if l=="":
            break
        lines.append([float(x) for x in l.split()])
    if lines:
        B1 = np.column_stack(lines)
        print("Enter second basis columns (same k):")
        lines2=[]
        while True:
            l=sys.stdin.readline().strip()
            if l=="":
                break
            lines2.append([float(x) for x in l.split()])
        if lines2 and len(lines2)==len(lines):
            B2 = np.column_stack(lines2)
            P = transition_matrix(B1, B2)
            print("Transition matrix P (B1 -> B2):\n", P)
        else:
            print("Skipped: second basis not provided or mismatched.")
    else:
        print("Skipping transition matrix demo.")

if __name__ == "__main__":
    main()
