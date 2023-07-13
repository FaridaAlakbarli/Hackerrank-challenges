#!/bin/python3

import math
import os
import random
import re
import sys


def happyLadybugs(b):
    # Write your code here
    count_ = b.count('_')

    for i in b:
        if i != '_'  and b.find(i) == b.rfind(i):
            return 'NO'

        count = b.count(i)
        if (b.find(i)+count)-1 != b.rfind(i) and count_ == 0:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    g = int(input('Enter number of games: ').strip())

    for g_itr in range(g):
        n = int(input('Enter number of cells: ').strip())

        b = input('Enter string: ')

        result = happyLadybugs(b)

        print(result)