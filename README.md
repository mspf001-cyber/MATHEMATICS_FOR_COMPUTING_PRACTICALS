# Mathematics-for-Computing - Practicals

Collection of Python scripts implementing the 13 practical exercises from "Mathematics for Computing" (Linear Algebra & Vector Calculus).
## Practical Table

| Practical No. | Title                                      | Description (What It Includes)                                                                 | File Name                                         |
|---------------|---------------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------|
| 1             | Vectors & Matrices                          | Vector/matrix creation, transpose, conjugate transpose, user input handling                      | practical_01_vectors_and_matrices.py              |
| 2             | Echelon Form & Rank                         | Row-echelon form (REF), custom row reduction, rank computation                                   | practical_02_echelon_rank.py                      |
| 3             | Cofactors, Determinant & Inverse            | Cofactor matrix, adjoint/adjuate, determinant, inverse (numeric & symbolic)                     | practical_03_cofactors_determinant_inverse.py     |
| 4             | Gaussian Elimination (Non-Homogeneous)      | Solve Ax = b using Gaussian elimination with partial pivoting                                    | practical_04_gauss_elimination_nonhom.py          |
| 5             | Gauss-Jordan (Homogeneous System)           | RREF, pivot detection, null-space basis extraction                                               | practical_05_gauss_jordan_hom.py                  |
| 6             | Subspaces & Transition Matrix               | Column space, row space, null space, left-null; optional transition matrix between bases         | practical_06_subspaces_basis_transition.py        |
| 7             | Linear Dependence & Transition Matrix       | Check linear dependence, rank test, compute transition matrix between bases                      | practical_07_linear_dependence_and_transition.py  |
| 8             | Gram-Schmidt Process                        | Orthonormal basis computation using classical Gram-Schmidt                                       | practical_08_gram_schmidt.py                      |
| 9             | Eigenvalues, Diagonalizability & C-H        | Eigenvalues/vectors, diagonalizability test, Cayley-Hamilton verification                        | practical_09_eigen_cayley_hamilton.py             |
| 10            | Matrix Coding & Decoding                    | Encode/decode messages using nonsingular matrices (mod 29)                                       | practical_10_coding_decoding.py                   |
| 11            | Gradient of a Scalar Field                  | Symbolic gradient calculation using sympy                                                        | practical_11_gradient_scalar_field.py             |
| 12            | Divergence of a Vector Field                | Symbolic divergence of n-dimensional vector field                                                | practical_12_divergence_vector_field.py           |
| 13            | Curl of a Vector Field                      | Symbolic curl computation for 3-D vector fields                                                  | practical_13_curl_vector_field.py                 |

## Dependencies
- Python 3.8+
- numpy
- sympy

Install dependencies:
```bash
pip install numpy sympy
