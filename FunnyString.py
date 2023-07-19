#!/bin/python3

import math
import os
import random
import re
import sys


def funnyString(s):
    # Write your code here
    value_list = []
    reverse_list = []
    for i in s:
        value_list.append(ord(i))
        reverse_list.insert(0, ord(i))

    answer = True

    for i in range(len(s)-1):
        if abs(value_list[i] - value_list[i+1]) != abs(reverse_list[i] - reverse_list[i+1]):
            answer = False
            break

    if answer:
        return 'funny'
    else:
        return 'not funny'

if __name__ == '__main__':

    s = input('Enter the string: ')

    result = funnyString(s)

    print(result)