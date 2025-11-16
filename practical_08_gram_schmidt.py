#!/usr/bin/env python3
"""
Practical 8
Compute orthonormal basis using Gram-Schmidt.
"""
import sys
import numpy as np

def read_vectors():
    print("Enter vectors (one per line, components space-separated). Blank -> example:")
    rows=[]
    while True:
        l=sys.stdin.readline().strip()
        if l=="":
            break
        rows.append([float(x) for x in l.split()])
    if not rows:
        return np.array([[1,1,0],[1,0,1],[0,1,1]], dtype=float).T
    return np.array(rows,dtype=float).T

def gram_schmidt(V):
    # V columns are vectors
    m,n = V.shape
    Q = np.zeros((m,n))
    for i in range(n):
        v = V[:,i].copy()
        for j in range(i):
            q = Q[:,j]
            v -= np.dot(q, v)*q
        norm = np.linalg.norm(v)
        if norm < 1e-12:
            Q[:,i] = np.zeros(m)
        else:
            Q[:,i] = v / norm
    # trim zero columns
    cols = [i for i in range(n) if np.linalg.norm(Q[:,i])>1e-12]
    if not cols:
        return np.zeros((m,0))
    return Q[:,cols]

def main():
    V = read_vectors()
    print("Input vectors (columns):\n", V)
    Q = gram_schmidt(V)
    print("\nOrthonormal basis (columns):\n", Q)

if __name__ == "__main__":
    main()
