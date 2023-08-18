#!/bin/python3

import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    # Write your code here
    set1 = set(s1)
    set2 = set(s2)

    intersection = set1.intersection(set2)
    if len(intersection) >= 1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    s1 = input('Enter the first string: ')

    s2 = input('Enter the second string: ')

    result = twoStrings(s1, s2)

