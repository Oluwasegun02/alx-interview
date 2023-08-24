#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """ Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return [] 

    pascal_list = []
    for i in range(n):
        row = [1] 

        for j in range(1, i):
            row.append(pascal_list[i - 1][j - 1] + pascal_list[i - 1][j])

        if i > 0:
            row.append(1)

        pascal_list.append(row)

    return pascal_list