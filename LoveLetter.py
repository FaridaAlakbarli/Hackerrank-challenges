#!/bin/python3

import math
import os
import random
import re
import sys


def theLoveLetterMystery(s):
    # Write your code here
    letters = 'abcdefghijklmnopqrstuvwxyz'
    length = len(s)
    last_index = len(s) - 1
    counter = 0
    for i in range(math.ceil(length/2)):
        left = s[i]
        right = s[last_index-i]
        counter += abs(letters.find(left) - letters.find(right))
    return counter

if __name__ == '__main__':

    s = input()

    result = theLoveLetterMystery(s)

    print(result)
