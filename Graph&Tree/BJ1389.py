from collections import deque
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M) :
    u, v = map(int, input().split())
    adj[u].append(v) ; adj[v].append(u)

def bfs(v,k) :
    d = 0
    queue = deque([(v, d)])

    while queue :
        c, d = queue.popleft()
        if c == k :
            return d
        if not visited[c] :
            d += 1
            visited[c] = True
            for n in adj[c] :
                if not visited[n] :
                    queue.append((n, d))

answer = []
for i in range(1, N+1) :
    nums = []
    for j in range(1, N+1) :
        visited = [False] * (N + 1)
        nums.append(bfs(i, j))
    answer.append(sum(nums))

print(answer.index(min(answer))+1)