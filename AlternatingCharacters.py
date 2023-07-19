#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    # Write your code here
    lis = []
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            lis.append(s[i])

    if len(lis) == 0:
        lis.append(s[0])

    if lis[-1] != s[-1]:
        lis.append(s[-1])


    return lis

if __name__ == '__main__':

    s = input('Enter the string: ')

    result = alternatingCharacters(s)

    print(result)
