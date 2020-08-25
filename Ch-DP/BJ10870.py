import sys

N = int(sys.stdin.readline())
memo = [0] * 20

def solve(n) :
    if n <= 1 :
        return n

    if memo[n] > 0 :
        return memo[n]

    memo[n] = solve(n-1) + solve(n-2)
    return memo[n]

print(solve(N))


def bottom_up(n) :
    d = [0] * 20
    d[0] = 0
    d[1] = 1
    for i in range(2,21) :
        d[i] = d[i-1] + d[i-2]
    return d[n]