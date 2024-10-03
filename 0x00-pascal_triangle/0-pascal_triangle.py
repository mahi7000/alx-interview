#!/usr/bin/python3
'''A module for Pascals Triangle'''


def pascal_triangle(n):
    '''Create a list of lists of integers that represent Pascal's Triangle'''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        tri = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tri.append(1)
            elif i > 0 and j > 0:
                tri.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(tri)
    return triangle
