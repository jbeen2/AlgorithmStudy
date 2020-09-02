N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0] * (N + 1)
sum[1] = nums[0]

for k in range(1, N):
    sum[k + 1] = sum[k] + nums[k]

for _ in range(M) :
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])