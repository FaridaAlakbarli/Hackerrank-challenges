#!/bin/python3

import math
import os
import random
import re
import sys


def palindromeIndex(s):
    if s == s[::-1]:
        return -1

    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            new = s[:i] + s[i + 1:]
            if new == new[::-1]:
                return i

            new = s[:len(s) - i - 1] + s[len(s) - i:]
            if new == new[::-1]:
                return len(s) - i - 1

    return -1


if __name__ == '__main__':

    s = input('Enter string: ')

    result = palindromeIndex(s)

    print(result)