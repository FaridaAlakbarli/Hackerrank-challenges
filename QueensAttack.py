#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    attack_directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    obstacles_set = {(obstacle[0], obstacle[1]) for obstacle in obstacles}

    attacked_squares = 0
    for dx, dy in attack_directions:
        x, y = r_q, c_q
        while True:
            x += dx
            y += dy

            if x > n or x < 1 or y > n or y < 1 or (x, y) in obstacles_set:
                break
            attacked_squares += 1
    return attacked_squares

if __name__ == '__main__':

    first_multiple_input = input('Enter first multiple input: ').rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input('Enter second multiple input: ').rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input('Enter obstacles: ').rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)