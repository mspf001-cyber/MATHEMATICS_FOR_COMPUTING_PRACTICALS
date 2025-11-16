#!/usr/bin/env python3
"""
Practical 13
Compute curl of a 3D vector field symbolically.
User provides components F = (P,Q,R).
"""
import sys
from sympy import symbols, sympify, Matrix

def main():
    print("This computes curl for 3 variables x y z by default.")
    print("Enter components P,Q,R separated by commas. Blank -> P=x*y, Q=y*z, R=z*x")
    cl = sys.stdin.readline().strip()
    if cl=="":
        comp_texts = ["x*y","y*z","z*x"]
    else:
        comp_texts = [c.strip() for c in cl.split(",")]
    x,y,z = symbols('x y z')
    if len(comp_texts) != 3:
        print("Need 3 components.")
        return
    P = sympify(comp_texts[0])
    Q = sympify(comp_texts[1])
    R = sympify(comp_texts[2])
    curl = Matrix([R.diff(y)-Q.diff(z), P.diff(z)-R.diff(x), Q.diff(x)-P.diff(y)])
    print("\nVector field F = (P,Q,R):", (P,Q,R))
    print("Curl(F):", curl)

if __name__ == "__main__":
    main()
