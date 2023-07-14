#!/bin/python3

import math
import os
import random
import re
import sys


def hackerrankInString(s):
    # Write your code here
    string = 'hackerrank'
    index_list = []
    start = 0

    for letter in string:
        index = s.find(letter, start)
        index_list.append(index)
        start = index + 1

    if index_list == sorted(index_list):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    s = input('Enter the string: ')

    result = hackerrankInString(s)

    print(result)