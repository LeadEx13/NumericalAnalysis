from copy import deepcopy
from datetime import datetime

SIZE = 3
epsilon = 0.0000000001


# returns the value of multiplying matrix m with vector v
def multiply_matrix_with_vector(m: list, v: list):
    solutions = []
    s = 0
    for row in m:
        for i in range(SIZE):
            s += (v[i] * row[i])
        solutions.append(s)
        s = 0
    return solutions


# returns an identity matrix based on n size
def identityMatrix(n):
    matrix = []
    for i in range(n):
        matrix.append([0 for _ in range(n)])
    for j in range(n):
        matrix[j][j] = 1
    return matrix


# returns the inverted A matrix
def invertMatrix(A):
    A_COPY = deepcopy(A)  # dont want to change the original A
    I = identityMatrix(len(A))
    indices = list(range(len(A)))

    for fd in range(len(A)):
        pivot = 1 / A_COPY[fd][fd]
        for j in range(len(A)):
            A_COPY[fd][j] *= pivot
            I[fd][j] *= pivot

        for i in indices[0:fd] + indices[fd + 1:]:
            crScaler = A_COPY[i][fd]
            for j in range(len(A)):
                A_COPY[i][j] = A_COPY[i][j] - crScaler * A_COPY[fd][j]
                I[i][j] = I[i][j] - crScaler * I[fd][j]
    return I


# returns the solution of Ax=B using the invert method
def invertMethod(A, B):
    A_INVERT = invertMatrix(A)
    print("\nThe inverted A: ")
    printMatrix(A_INVERT)

    X = multiply_matrix_with_vector(A_INVERT, B)
    print("\nThe result of (inverted A * V) is: ")
    X = list(map(
        lambda v: str(v) + f"00000{datetime.now().day}{datetime.now().time().hour}{datetime.now().time().minute}",
        X
    ))
    print(X)


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
def pivot_matrix(m: list):
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
def jacobi_method(m: list, vector: list):
    temp_values = [0 for _ in range(SIZE)]
    values = solveJacobiEquation(m, vector, temp_values)

    while abs(values[0] - temp_values[0]) > epsilon:
        temp_values = deepcopy(values)
        values = solveJacobiEquation(m, vector, temp_values)
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

    print("\nMETHOD 1: JACOBI METHOD")

    # pivoting and dominant diagonal
    NEW_A = pivot_matrix(A)
    NEW_A = createDominantDiagonal(NEW_A)
    print("Matrix A after pivot and creating dominant diagonal: ")
    printMatrix(NEW_A)

    print("\nStarting to print iterations..")
    values = jacobi_method(NEW_A, solution_vector)
    print("\nThe result of jacobi method is: ")
    values = list(map(
        lambda v: str(v) + f"00000{datetime.now().day}{datetime.now().time().hour}{datetime.now().time().minute}",
        values
    ))
    print(values)

    print("\n\nMETHOD 2 : INVERT METHOD")
    invertMethod(A, solution_vector)


if __name__ == '__main__':
    main()
