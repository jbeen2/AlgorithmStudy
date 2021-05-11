N = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]
dp[0][nums[0]] += 1

for i in range(1, N-1) :
    for j in range(21) :
        if dp[i-1][j] :
            if j + nums[i] <= 20 :
                dp[i][j + nums[i]] += dp[i-1][j]
            if j - nums[i] >= 0 :
                dp[i][j - nums[i]] += dp[i-1][j]

print(dp[N-2][nums[-1]])


# ============= Time Exceed =============
eq = [[nums[0]]]
for i in range(1, N-1) :
    tmp = []
    for e in eq[i-1] :
        if e+nums[i] <= 20 :
            tmp.append(e+nums[i])
        if e-nums[i] >= 0 :
            tmp.append(e-nums[i])
    eq.append(tmp)

print(len([e for e in eq[-1] if e == nums[-1]]))