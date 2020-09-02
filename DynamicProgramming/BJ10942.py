import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

def solve(S,E) :
    if S > E :
        return 0

    if S == E :
        return 1
    elif (E-S) == 1 :
        if num[S] == num[E] :
            return 1
        return 0

    if memo[S][E] != -1 :
        return memo[S][E]
    if num[S] == num[E] :
        memo[S][E] = solve(S+1, E-1)
        return memo[S][E]
    return 0

memo = [[-1] * (N+1) for _ in range(N+1)]
for _ in range(M) :
    S, E = map(int, sys.stdin.readline().split())
    print(solve(S-1,E-1))