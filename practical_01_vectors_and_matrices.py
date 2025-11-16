Practical 1
Create and transform vectors and matrices:
- transpose
- conjugate transpose (Hermitian)
Prompts user for vector/matrix input.
"""
import numpy as np
import sys

def read_matrix(prompt="Enter matrix rows (each row on a new line). Blank line to finish:"):
    print(prompt)
    rows = []
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        parts = line.split()
        rows.append([complex(x) for x in parts])
    if not rows:
        # test default
        return np.array([[1,2+1j],[3,4]])
    return np.array(rows)

def main():
    M = read_matrix("Enter matrix rows (space-separated). Blank line to finish (empty -> default example):")
    print("Matrix (M):\n", M)
    print("\nTranspose M^T:\n", M.T)
    print("\nConjugate transpose (Hermitian) M^*:\n", M.conj().T)
    # vector handling: allow single-row or single-column
    print("\nNow enter a vector (space-separated). Blank line -> default [1,2,3]:")
    vline = sys.stdin.readline().strip()
    if vline == "":
        v = np.array([1,2,3])
    else:
        v = np.array([complex(x) for x in vline.split()])
    print("Vector v:", v)
    print("v as column:\n", v.reshape((-1,1)))
    print("v as row:\n", v.reshape((1,-1)))
    print("v transpose:", v.T)
    print("v conjugate transpose:", v.conj().T)

if __name__ == "__main__":
    main()
