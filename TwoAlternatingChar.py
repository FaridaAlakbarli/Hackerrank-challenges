#!/bin/python3

import math
import os
import random
import re
import sys


def alternate(s):
    # Write your code here
    unique_chars = list(set(s))
    new_string = ''
    length = []

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            temp_string = unique_chars[i] + unique_chars[j]

            for k in s:
                if k in temp_string:
                    new_string += k

            length.append(len(new_string))

            for j in range(len(new_string) - 2):
                if new_string[j] != new_string[j + 2]:
                    length.remove(len(new_string))
                    break
            new_string = ''

    if len(length) == 0:
        return 0
    else:
        return max(length)

if __name__ == '__main__':

    s = input('Enter string: ')

    result = alternate(s)

    print(result)