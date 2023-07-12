#!/bin/python3

import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    # Write your code here
    page = 0
    special = 0
    for chapter in arr:
        for j in range(1, chapter + 1):
            if k != 1:
                if j % k == 1:
                    page += 1
                if j == page:
                    special += 1
            else:
                page += 1
                if j == page:
                    special += 1

    return special

if __name__ == '__main__':

    first_multiple_input = input('Enter two numbers: ').rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input('Enter numbers: ').rstrip().split()))

    result = workbook(n, k, arr)
    print(result)

