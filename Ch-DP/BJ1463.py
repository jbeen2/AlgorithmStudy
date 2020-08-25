import sys
sys.setrecursionlimit(10**6)

memo = [0] * 1231231

def solve(n) :
    if n < = 3 :
        return 1

    if memo[n] > 0 :
        return memo[n]

    