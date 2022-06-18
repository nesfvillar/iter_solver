def jacobi(unknowns, functions, max_iter = 500, tolerance = 0.001):
    if len(unknowns) != len(functions):
        raise ValueError('Number of variables is not the same as number of functions')

    solution = prev_solution = unknowns
    for i in range(max_iter):
        solution = [function(prev_solution) for function in functions]

        exit = [abs(current - previous) < tolerance for current, previous in zip(solution, prev_solution)]
        if all(exit):
            return solution
        else:
            prev_solution = solution

    raise ValueError(f'The solution did not converge after {max_iter} iterations for tolerance {tolerance}')


def gauss_seidel(unknowns, functions, max_iter = 500, tolerance = 0.001):
    if len(unknowns) != len(functions):
        raise ValueError('Number of variables is not the same as number of functions')

    solution = unknowns
    prev_solution = solution.copy()
    for i in range(max_iter):
        for j, function in enumerate(functions):
            solution[j] = function(solution)

        exit = [abs(current - previous) < tolerance for current, previous in zip(solution, prev_solution)]
        if all(exit):
            return solution
        else:
            prev_solution = solution.copy()

    raise ValueError(f'The solution did not converge after {max_iter} iterations for tolerance {tolerance}')


def main():
    def f(args):
        x, y, z = args
        return (10 - y - 2 * z) / 7

    def g(args):
        x, y, z = args
        return (8 - x - 3 * z) / 8


    def h(args):
        x, y, z = args
        return (6 - 2 * x - 3 * y) / 9

    unknowns = [0, 0, 0]
    functions = [f, g, h]
    tolerance = 1e-9

    solution = jacobi(unknowns, functions, tolerance=tolerance)
    print(solution)

    solution = gauss_seidel(unknowns, functions, tolerance=tolerance)
    print(solution)


if __name__ == '__main__':
    main()
