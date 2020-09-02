N, S, M = map(int, input().split())
V = list(map(int, input().split()))

prev, next = [0] * (M+1) , [0] * (M+1)
prev[S] = 1

for vol in V :
    for i in range(M+1) :
        if prev[i] == 1 :
            if i+vol <= M :
                next[i+vol] = 1
            if i-vol >= 0 :
                next[i-vol] = 1

    prev = next
    next = [0] * (M+1)


answer = -1
for p in range(M,-1,-1):
    if prev[p] == 1 :
        answer = p
        break

print(answer)


# 메모리 초과 ^_^
prev = []
prev.append(S)


for i in range(N) :
    next = []

    # list comprehension의 문제가 아님...
    next.extend([p+V[i] for p in prev if 0<=p+V[i]<=M])
    next.extend([p-V[i] for p in prev if 0<=p-V[i]<=M])

    # .copy() 문제 또한 아님...
    del prev
    prev = next.copy()

    if len(prev) == 0 :
        break
        print(-1)

print(max(next) if len(next)!=0 else -1)