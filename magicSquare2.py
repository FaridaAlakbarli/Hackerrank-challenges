# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    matrix = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    ]

    lis = []

    for item in matrix:
        count = 0
        for i in range(3):
            for j in range(3):
                count += abs(item[i][j] - s[i][j])
        lis.append(count)

    return min(lis)


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input('Enter 3 numbers: ').rstrip().split())))

    result = formingMagicSquare(s)

    print(result)