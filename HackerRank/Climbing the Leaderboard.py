# Time Limit Exceed...

# !/bin/python3

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
    def dense_ranking(ranked, p=False, rerank=False):
        if rerank:
            ranked.append(p)

        temp = [(idx + 1, score) for idx, score in enumerate(sorted(list(set(ranked)), reverse=True))]
        ranking = []
        for r in ranked:
            for t in temp:
                if r == t[1]:
                    ranking.append(t[0])

        return ranking

    dense_ranking(ranked)
    answer = [dense_ranking(ranked, p, rerank=True)[-1] for p in player]
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
