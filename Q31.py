###### Q31 ######

import sympy as sp
from sympy import Symbol
from datetime import datetime


# returns the m (slope) between 2 points
def find_slope(p1: tuple, p2: tuple):
    y = p2[1] - p1[1]
    x = p2[0] - p1[0]
    m = y / x
    print(f"The slope for p1{p1} and p2{p2} is: {m}")
    return m


# returns the L(x) for position i
def find_L(points: list, i: int, x: Symbol):
    f = 1
    for j in range(len(points)):
        # only if i != j we add the next equation
        if j != i:
            f *= (x - points[j][0]) / (points[i][0] - points[j][0])
    return f


# takes 2 points which our value is in between, and creates a linear equation
# from that equation we return the result by assigning the value
def linear_method(points: list, value):
    result = None
    for i in range(len(points)):
        if points[i][0] > value:
            point1 = points[i - 1]
            point2 = points[i]
            m = find_slope(point1, point2)
            x = sp.symbols('x')
            f = m * x + (point1[1] - m * point1[0])
            print(f"The linear equation for points p1{point1} and p2{point2} is: y = {f}")
            result = sp.lambdify(x, f)(value)
            break

    return result


# we generate a polynom created from the sum of Li(x) using the formula
# after the polynom is created, we assign the value and return the result
def lagrange_method(points: list, value):
    f = 0
    x = sp.symbols('x')
    for i in range(len(points)):
        l = find_L(points, i, x)
        print(f"L{i}(x): {l}")
        f += l * points[i][1]  # Li(x) * Yi

    print(f"\nThe final polynom π of Li(x):")
    print(f)
    return sp.lambdify(x, f)(value)


# the main method
def main():
    points = [(1.2, 1.5095), (1.3, 1.6984), (1.4, 1.9043), (1.5, 2.1293), (1.6, 2.3756)]
    x = 1.47  # the x we will recieve the f(x) to

    print(f"The points: {points}")
    print(f"The x to calculate: {x}")

    print("\nMethod 1: Linear method")
    result_linear = linear_method(points, x)
    calculation_time = f"{datetime.now().day}{datetime.now().time().hour}{datetime.now().time().minute}"
    print(f"the result of f({x}) is:  {result_linear}00000{calculation_time}")

    print("\n\nMethod 2: Lagrange method")
    result_lagrange = lagrange_method(points, x)
    calculation_time = f"{datetime.now().day}{datetime.now().time().hour}{datetime.now().time().minute}"
    print(f"the result of f({x}) is:  {result_lagrange}00000{calculation_time}")
    print('\033[92m' + "\n\nProgram finished! Exiting..")


if __name__ == '__main__':
    main()
