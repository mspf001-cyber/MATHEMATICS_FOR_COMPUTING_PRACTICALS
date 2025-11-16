#!/usr/bin/env python3
"""
Practical 7
Check linear dependence of given vectors and compute transition matrix between two bases.
"""
import sys
import numpy as np

def read_vectors():
    print("Enter vectors (one per line, components space-separated). Blank to use example:")
    vecs=[]
    while True:
        l=sys.stdin.readline().strip()
        if l=="":
            break
        vecs.append([float(x) for x in l.split()])
    if not vecs:
        return np.array([[1,2,3],[2,4,6],[1,0,1]],dtype=float).T
    return np.array(vecs,dtype=float).T

def is_dependent(V):
    rank = np.linalg.matrix_rank(V)
    cols = V.shape[1]
    return rank < cols

def transition_matrix(B_from, B_to):
    P, *_ = np.linalg.lstsq(B_from, B_to, rcond=None)
    return P

def main():
    V = read_vectors()
    print("Vectors as columns:\n", V)
    dep = is_dependent(V)
    print("Linear dependence:", dep)
    if dep:
        print("Rank:", np.linalg.matrix_rank(V), "Number of vectors:", V.shape[1])
    else:
        print("Vectors are linearly independent.")
    print("\nOptional: compute transition matrix. Enter base1 then base2, each vector per line, blank to skip.")
    print("Base1:")
    b1=[]
    while True:
        l=sys.stdin.readline().strip()
        if l=="":
            break
        b1.append([float(x) for x in l.split()])
    if not b1:
        print("Skipping transition matrix.")
        return
    print("Base2:")
    b2=[]
    while True:
        l=sys.stdin.readline().strip()
        if l=="":
            break
        b2.append([float(x) for x in l.split()])
    B1 = np.column_stack(b1)
    B2 = np.column_stack(b2)
    if B1.shape != B2.shape:
        print("Bases must have the same shape.")
        return
    P = transition_matrix(B1, B2)
    print("Transition matrix P such that B2 = B1 * P:\n", P)

if __name__ == "__main__":
    main()
