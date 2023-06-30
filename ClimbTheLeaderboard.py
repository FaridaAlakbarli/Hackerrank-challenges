#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    new_ranked = list(sorted(set(ranked), reverse=True))

    rank = []
    l = len(new_ranked)

    for score in player:
        right = l
        left = 0
        while left < right:
            mid = (right + left) // 2
            if new_ranked[mid] == score:
                left = mid
                break
            elif new_ranked[mid] < score:
                right = mid
            else:
                left = mid + 1
        rank.append(left + 1)

    return rank


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)
