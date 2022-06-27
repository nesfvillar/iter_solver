# Gauss-Seidel and Jacobi methods

The Gauss-Seidel and Jacobi methods are iterative methods for solving a set of equations.
Althoug there is no guarantee that the solution ever converges, the methods are easy to
implement and work on some certain non-linear equations.

The main difference between the Gauss-Seidel and Jacobi methods is that the first one
uses the newest values of the solution on each iteration, while the Jacobi method uses
the values of the previous loop.

This branch works on matrices and vectors, so the linear algebra aspect of the iterative
solver.

# Example

```python
import iter_solve as is

matrix = [[10, 2, 3],
          [4, 11, 6],
          [7, 8, 90]]

vector = [10, 11, 12]


solutions = is.gauss_seidel(matrix, vector)
print(solutions)
```