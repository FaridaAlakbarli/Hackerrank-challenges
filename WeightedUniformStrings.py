#!/bin/python3

import math
import os
import random
import re
import sys


def weightedUniformStrings(s, queries):
    # Write your code here
    letter_string = 'abcdefghijklmnopqrstuvwxyz'
    weights = set()
    outputs = []
    prev_letter = ''

    for letter in s:
        if letter != prev_letter:
            weight = letter_string.find(letter) + 1
            prev_letter = letter
        else:
            weight += letter_string.find(letter) + 1
        weights.add(weight)

    for query in queries:
        if query in weights:
            outputs.append('Yes')
        else:
            outputs.append('No')

    return outputs

if __name__ == '__main__':

    s = input('Enter the string: ')

    queries_count = int(input('Enter the number of queries: ').strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input('Enter query item: ').strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    print(result)