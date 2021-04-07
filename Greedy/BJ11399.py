N = int(input())
time = sorted(list(map(int, input().split())))

def cumsum(x) :
    total = 0
    for i in x :
        total += i
    return total

answer = 0
for t in range(len(time)+1) :
    answer += cumsum(time[:t])

print(answer)

# ============================

answer = 0
for i in range(N):
    answer += time[i] * (N-i)

print(answer)
