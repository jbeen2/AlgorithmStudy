N = int(input())
price = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = price[1]

for i in range(2, N + 1):
    dp[i] = price[i]
    for j in range(1, i // 2 + 1):
        if dp[i] <= dp[j] + dp[i - j]:
            dp[i] = dp[j] + dp[i - j]

print(dp[-1])