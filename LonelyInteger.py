#!/bin/python3

import math
import os
import random
import re
import sys


def lonelyinteger(a):
    # Write your code here

    for i in a:
        if a.count(i) == 1:
            return i


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

