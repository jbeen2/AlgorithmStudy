n = int(input())
nums = list(map(int, input().split()))
sum = [nums[0]]

for i in range(n-1) :
    sum.append(max(sum[i]+nums[i+1], nums[i+1]))

print(max(sum))



# 이렇게 하는게 아니래 ^_^ ㅎㅎㅎ
for k in range(1, n):
    sum[k + 1] = sum[k] + nums[k]


a, b = max(sum[1:]), min(sum[1:])
if sum.index(a) > sum.index(b) :
    print(a-b)
else :
    maxcheck = a - min(sum[1:sum.index(a)+1])
    mincheck = max(sum[sum.index(a)+1:]) - b
    print(max(maxcheck, mincheck))