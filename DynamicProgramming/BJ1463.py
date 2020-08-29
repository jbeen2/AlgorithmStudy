n = int(input())
d = [0] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i%2 == 0 and d[i] > d[i//2] + 1 :
        d[i] = d[i//2] + 1
    if i%3 == 0 and d[i] > d[i//3] + 1 :
        d[i] = d[i//3] + 1

print(d[n])




# 재귀로 풀면 메모리초과 뜬당 ㅎㅎㅎㅎㅎ

# def solve(n) :
#     if memo[n] > 0:
#         return memo[n]
#
#     if n<=3 :
#         memo[n] = 1
#         return memo[n]
#
#     if n % 3 == 0:
#         memo[n] = min(solve(n//3) + 1, solve(n-1) + 1)
#         return memo[n]
#
#     if n % 2 == 0:
#         memo[n] = min(solve(n//2) + 1, solve(n-1) + 1)
#         return memo[n]
#
#     if n % 6 == 0:
#         memo[n] = min(solve(n//3) + 1, solve(n//2) + 1, solve(n-1) + 1)
#         return memo[n]
#
#     memo[n] = solve(n-1) + 1
#     return memo[n]
#
# print(solve(n))

# def solve(n):
#     if memo[n] > 0:
#         return memo[n]
#
#     if n <= 3:
#         memo[n] = 1
#         return memo[n]
#
#     if n % 3 == 0:
#         a = solve(n // 3) + 1
#     else:
#         a = 1000001
#
#     if n % 2 == 0:
#         b = solve(n // 2) + 1
#     else:
#         b = 1000001
#
#     c = solve(n - 1) + 1
#
#     memo[n] = min(a, b, c)
#     return memo[n]