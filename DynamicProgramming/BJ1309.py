N = int(input())
dp = [0] * 100001
dp[0], dp[1] = 1, 3

for i in range(2, N+1) :
    dp[i] = dp[i-1] + 2*dp[i-2] + (dp[i-1] - dp[i-2])
    dp[i] %= 9901

print(dp[N])