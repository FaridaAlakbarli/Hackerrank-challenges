#!/bin/python3

import math
import os
import random
import re
import sys


def maximizingXor(l, r):
    # Write your code here
    xor = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            if xor < i^j:
                xor = i^j

    return xor

if __name__ == '__main__':

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    print(result)