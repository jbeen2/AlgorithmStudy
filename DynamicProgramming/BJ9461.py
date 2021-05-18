dp = [1, 1, 1] + [0]*97
for i in range(3, 100) :
    dp[i] = dp[i-2] + dp[i-3]

T = int(input())
for _ in range(T) :
    n = int(input())
    print(dp[n-1])