#!/bin/python3

import math
import os
import random
import re
import sys


def gameOfThrones(s):
    # Write your code here
    string_set = set(s)
    flag = 0

    for i in string_set:
        if s.count(i) % 2 == 1:
            flag += 1

    if flag > 1:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':

    s = input('Enter the string: ')

    result = gameOfThrones(s)
    print(result)