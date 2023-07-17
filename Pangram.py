#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lis = list(set(s.lower()))
    lis.sort()
    if ' ' in lis:
        lis.remove(' ')
    new_string = ''.join(lis)


    if new_string == alphabet:
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':

    s = input('Enter string: ')

    result = pangrams(s)

    print(result)