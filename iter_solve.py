def jacobi(matrix, vector, max_iter=100, tolerance=1e-9):
    n = len(vector)
    solution = [0] * n
    residual = [0] * n
    for it in range(max_iter):
        for i in range(n):
            residual[i] = vector[i] - sum([matrix[i][j] * solution[j] for j in range(n)])
        for i in range(n):
            solution[i] += residual[i]/matrix[i][i]
        if all([abs(r/matrix[i][i]) < tolerance for i, r in enumerate(residual)]):
            return solution

    raise ValueError(f'The solution did not converge after {max_iter} iterations for tolerance {tolerance}')


def gauss_seidel(matrix, vector, max_iter=100, tolerance=1e-9):
    n = len(vector)
    solution = [0] * n
    residual = [0] * n
    for it in range(max_iter):
        for i in range(n):
            residual[i] = vector[i] - sum([matrix[i][j] * solution[j] for j in range(n)])
            solution[i] += residual[i]/matrix[i][i]
        if all([abs(r/matrix[i][i]) < tolerance for i, r in enumerate(residual)]):
            return solution

    raise ValueError(f'The solution did not converge after {max_iter} iterations for tolerance {tolerance}')


def main():
    matrix = [[10, 2, 3],
              [4, 11, 6],
              [7, 8, 90]]

    vector = [10, 11, 12]

    jacobi_sol = jacobi(matrix, vector)
    gauss_sol = gauss_seidel(matrix, vector)

    print(f'Jacobi solution: {jacobi_sol}')
    print(f'Gauss-Seidel solution: {gauss_sol}')
    print(f'Difference: {[j - g for j, g in zip(jacobi_sol, gauss_sol)]}')


if __name__ == '__main__':
    main()
