#!/bin/python3

import math
import os
import random
import re
import sys


def marsExploration(s):
    # Write your code here
    count = 0
    sos = 'SOS'

    for i in range(0, len(s) - 2, 3):
        sos_string = s[i:i + 3]
        if sos_string == 'SOS':
            pass
        else:
            for j in range(3):
                if sos[j] != sos_string[j]:
                    count += 1

    return count


if __name__ == '__main__':

    s = input('Enter string: ')

    result = marsExploration(s)

    print(result)