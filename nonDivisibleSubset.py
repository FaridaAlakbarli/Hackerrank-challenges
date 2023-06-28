#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    remainders = [0] * k
    counter = 0
    for num in s:
        remainders[num % k] += 1

    if remainders[0] != 0:
        counter += 1

    for i in range(1, math.ceil(k / 2)):
        counter += max(remainders[i], remainders[-i])

    if k % 2 == 0:
        counter += 1

    return counter

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)