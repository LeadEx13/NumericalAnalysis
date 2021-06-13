from copy import deepcopy

SIZE = 3
epsilon = 0.0000000001


# prints matrix
def printMatrix(m):
    for row in m:
        print([item for item in row])


# prints vector
def printVector(v):
    print([float("{:.10f}".format(item)) for item in v])


def swapColumns(m: list, i, j):
    matrix = deepcopy(m)
    size = len(matrix)
    for k in range(size):
        for l in range(size):
            if l == i:
                temp = matrix[k][l]
                matrix[k][l] = matrix[k][j]
                matrix[k][j] = temp
    return matrix


# returns True if matrix has a dominant diagonal,
# or we succeeded creating a dominant diagonal - else False
def createDominantDiagonal(m: list):
    # BRUTE FORCE!
    matrix = deepcopy(m)
    for i in range(SIZE):
        for j in range(SIZE):
            if isDominantDiagonal(matrix):
                return matrix
            if i != j:
                matrix = swapRows(m, i, j)
            for k in range(SIZE):
                for l in range(SIZE):
                    if isDominantDiagonal(matrix):
                        return matrix
                    if k != l:
                        matrix = swapColumns(m, k, l)
    return matrix


# returns True if the matrix has a dominant diagonal - else False
def isDominantDiagonal(m: list):
    for i in range(SIZE):
        if (sum(m[i]) - m[i][i]) > m[i][i]:
            return False
    return True


# swap rows i and j in given matrix
def swapRows(m: list, i: int, j: int):
    matrix = deepcopy(m)
    temp = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = temp
    return matrix


# transforms the given matrix into a pivot matrix
# returns the pivoted matrix
def pivotMatrix(m: list):
    for i in range(SIZE):
        max_value = 0
        index = 0
        for j in range(i, SIZE):
            if m[j][i] > max_value:
                max_value = m[j][i]
                index = j
        if index != i:
            m = swapRows(m, index, i)
    return m


# isolate the variable and returns the solution
# e.g: 4x +3y = 5 --> x = (5-3y) / 4
def getValue(variable: int, lst: list, sol: int, values: list):
    for i in range(len(lst)):
        sol -= (lst[i] * values[i])
    sol /= variable
    return sol


# returns the current list of values from the iteration
def solveJacobiEquation(m: list, vector: list, temp_values):
    values = deepcopy(temp_values)
    printVector(values)
    for i in range(SIZE):
        if i < SIZE - 1:
            values[i] = getValue(m[i][i],
                                 m[i][:i] + m[i][i + 1:],
                                 vector[i],
                                 temp_values[:i] + temp_values[i + 1:])
        else:
            values[i] = getValue(m[i][i],
                                 m[i][:i],
                                 vector[i],
                                 temp_values[:i])
    return values


# recieves a matrix and a solutions vector - solves the equation using Yaakobi Method
# returns the values based on the stop condition
# stop condition => x(r+1) - x(r) < epsilon
# we declared epsilon in the start of the file
def yaakobiMethod(m: list, vector: list):
    temp_values = [0 for _ in range(SIZE)]
    values = solveJacobiEquation(m, vector, temp_values)

    while abs(values[0] - temp_values[0]) > epsilon:
        temp_values = deepcopy(values)
        values = solveJacobiEquation(m, vector, temp_values)
    return values


# returns the current list of values from the iteration
def solveGausSeidelEquation(m: list, vector: list, temp_values):
    values = deepcopy(temp_values)
    printVector(values)
    for i in range(SIZE):
        if i < SIZE - 1:
            values[i] = getValue(m[i][i],
                                 m[i][:i] + m[i][i + 1:],
                                 vector[i],
                                 values[:i] + values[i + 1:])
        else:
            values[i] = getValue(m[i][i],
                                 m[i][:i],
                                 vector[i],
                                 values[:i])
    return values


# recieves a matrix and a solutions vector - solves the equation using Gaus Seidel Method
# returns the values based on the stop condition
# stop condition => x(r+1) - x(r) < epsilon
# we declared epsilon in the start of the file
def gausSeidelMethod(m: list, vector: list):
    temp_values = [0 for _ in range(SIZE)]
    values = solveGausSeidelEquation(m, vector, temp_values)

    while abs(values[0] - temp_values[0]) > epsilon:
        temp_values = deepcopy(values)
        values = solveGausSeidelEquation(m, vector, temp_values)

    return values


def main():
    A = [
        [10, 8, 1],
        [4, 10, -5],
        [5, 1, 10]
    ]
    solution_vector = [-7, 2, 1.5]

    # printing the variables
    print("A:")
    printMatrix(A)
    print(f"\nSolutions vector:\n{solution_vector}\n")

    # pivoting and dominant diagonal
    A = pivotMatrix(A)
    A = createDominantDiagonal(A)
    print("Matrix A after pivot and creating dominant diagonal: ")
    printMatrix(A)

    print("\nMETHOD 1: YAAKOBI METHOD")
    print("\nStarting to print iterations..")
    values = yaakobiMethod(A, solution_vector)
    print("\nThe result of yaakobi method is: ")
    printVector(values)

    print("\n\nMETHOD 2 : GAUS SEIDEL METHOD")
    values = gausSeidelMethod(A, solution_vector)
    print("\nThe result of gaus seidel method is: ")
    printVector(values)


if __name__ == '__main__':
    main()
