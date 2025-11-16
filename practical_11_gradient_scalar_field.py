#!/usr/bin/env python3
"""
Practical 11
Compute gradient of a scalar field symbolically using sympy.
User provides variables and scalar function as expression.
Example input:
variables: x y z
function: x**2 + y*z + sin(x)
"""
import sys
from sympy import symbols, sympify, Matrix

def main():
    print("Enter variables separated by space (e.g. x y z). Blank -> x y z")
    vars_line = sys.stdin.readline().strip()
    if vars_line=="":
        var_names = ["x","y","z"]
    else:
        var_names = vars_line.split()
    vars_sym = symbols(var_names)
    print("Enter scalar function in these variables (python syntax). Blank -> x**2 + y*z + sin(x):")
    fline = sys.stdin.readline().strip()
    if fline=="":
        fline = "x**2 + y*z + sin(x)"
    f = sympify(fline)
    grad = [f.diff(v) for v in vars_sym]
    print("\nScalar function f = ", f)
    print("Gradient ∇f (components):")
    for v, comp in zip(var_names, grad):
        print(f"d/d{v}:", comp)

if __name__ == "__main__":
    main()
