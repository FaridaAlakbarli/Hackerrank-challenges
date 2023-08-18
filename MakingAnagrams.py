#!/bin/python3

import math
import os
import random
import re
import sys


def makingAnagrams(s1, s2):
    l = len(s1 + s2)
    common_letters = ''
    i = 0
    j = 0
    l1 = len(s1)
    l2 = len(s2)

    while i < l1:
        while j < l2:
            if s1[i] == s2[j]:
                common_letters += s1[i]
                s1 = s1[:i] + s1[i + 1:]
                s2 = s2[:j] + s2[j + 1:]
                l1 = len(s1)
                l2 = len(s2)
                i = 0
                j = 0
                l -= 2

            if j == l2 - 1:
                j = 0
                break

            j += 1
        i += 1

    return l

if __name__ == '__main__':

    s1 = input('Enter the first string: ')

    s2 = input('Enter the second string: ')

    result = makingAnagrams(s1, s2)

    print(result)
