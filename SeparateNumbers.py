#!/bin/python3

import math
import os
import random
import re
import sys


def separateNumbers(s):
    # Write your code here
    n = len(s)
    answer = False

    for i in range(1, n // 2 + 1):
        substring = int(s[:i])
        temp = str(substring)
        while len(temp) < n:
            substring += 1
            temp += str(substring)
        if temp == s:
            answer = True
            break

    if answer:
        print('YES', s[:i])
    else:
        print('NO')


if __name__ == '__main__':

    s = input('Enter string: ')

    separateNumbers(s)

