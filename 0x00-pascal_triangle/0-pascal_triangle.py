#!/usr/bin/python3
def pascal_triangle(n):
    """ Create a function def pascal_triangle(n) that 
        Return an empty list for n <= 0
        if n is positive integer returns a list of lists
        where each inner list is a row of the Pascal's triangle
        starting from the top row.
        First element of each row is always 1
        Last element of each row is always 1
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