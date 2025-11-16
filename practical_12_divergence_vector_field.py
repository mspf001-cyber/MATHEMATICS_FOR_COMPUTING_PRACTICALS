#!/usr/bin/env python3
"""
Practical 12
Compute divergence of a vector field symbolically.
User supplies variables and vector components.
Example:
variables: x y z
components: x*y, y**2, z
"""
import sys
from sympy import symbols, sympify

def main():
    print("Enter variables separated by space (e.g. x y z). Blank -> x y z")
    vars_line = sys.stdin.readline().strip()
    if vars_line=="":
        var_names=["x","y","z"]
    else:
        var_names=vars_line.split()
    vars_sym = symbols(var_names)
    print(f"Enter components of vector field separated by commas (count = {len(var_names)}). Blank -> x*y, y**2, z")
    cl = sys.stdin.readline().strip()
    if cl=="":
        comp_texts = ["x*y","y**2","z"]
    else:
        comp_texts = [c.strip() for c in cl.split(",")]
    if len(comp_texts) != len(var_names):
        print("Number of components must equal number of variables.")
        return
    comps = [sympify(c) for c in comp_texts]
    div = sum([comps[i].diff(vars_sym[i]) for i in range(len(vars_sym))])
    print("\nVector field components:", comps)
    print("Divergence:", div)

if __name__ == "__main__":
    main()
