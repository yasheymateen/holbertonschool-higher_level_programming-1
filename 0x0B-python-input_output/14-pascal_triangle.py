#!/usr/bin/python3
"""pascal_triangle module"""


def pascal_triangle(n):
    """function that returns a list of lists of integers representing
    the Pascal’s triangle of n
    If n <= 0, returns empty list
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for row in range(2, n):
        prev = triangle[-1]
        new = [1]
        for i in range(1, row):
            num = prev[i - 1] + prev[i]
            new.append(num)
        new.append(1)
        triangle.append(new)
    return triangle
