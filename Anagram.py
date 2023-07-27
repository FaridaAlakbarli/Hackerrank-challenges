#!/bin/python3

import math
import os
import random
import re
import sys


def anagram(s):
    # Write your code here
    if len(s)%2 != 0:
        return -1

    left = s[:len(s)//2]
    right = s[len(s)//2:]
    l = len(left)
    i = 0
    j = 0

    while i < l:

        while j < l:
            x = left[i]
            y = right[j]
            if x == y:
                left = left[:i] + left[i+1:]
                right = right[:j] + right[j+1:]
                l = len(left)

                if l == 1 and left == right:
                    return 0
                j = 0
                break

            if j == l - 1:
                if i == l - 1:
                    return l
                else:
                    j = 0
                    i += 1
            else:
                j += 1

    return l



if __name__ == '__main__':
    s = input('Enter the string: ')

    result = anagram(s)

    print(result)