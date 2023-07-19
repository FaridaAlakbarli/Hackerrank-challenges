#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    l = len(b)
    lis = list(b)
    counter = 0
    for i in range(l-2):
        sublist = lis[i:i+3]
        if sublist == ['0','1','0']:
            lis[i+2] = '1'
            counter += 1

    return counter

if __name__ == '__main__':

    b = input('Enter the string: ')

    result = beautifulBinaryString(b)

    print(result)