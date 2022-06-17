# Gauss-Seidel and Jacobi methods

The Gauss-Seidel and Jacobi methods are iterative methods for solving a set of equations.
Althoug there is no guarantee that the solution ever converges, the methods are easy to
implement and work on some certain non-linear equations.

The main difference between the Gauss-Seidel and Jacobi methods is that the first one
uses the newest values of the solution on each iteration, while the Jacobi method uses
the values of the previous loop.

# Example

```python
import iter_solve as is

def f(args):
    x, y, z = args
    return (10 - y - 2 * z) / 7


def g(args):
    x, y, z = args
    return (8 - x - 3 * z) / 8


def h(args):
    x, y, z = args
    return (6 - 2 * x - 3 * y) / 9

guesses = [0, 0, 0]
functions = [f, g, h]

solutions = gauss_seidel(guesses, functions)
print(solutions)
```