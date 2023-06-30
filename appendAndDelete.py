#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    if k >= len(s) + len(t):
        return 'Yes'

    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1

    ops = len(s) - i + len(t) - i
    if ops <= k and (k - ops) % 2 == 0:
        return 'Yes'

    return 'No'


if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)
