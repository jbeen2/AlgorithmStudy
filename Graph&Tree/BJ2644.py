from collections import deque
n = int(input())
i, j = map(int, input().split())
m = int(input())

visited, adj = [False] * (n+1) , [[] for _ in range(n+1)]
for _ in range(m) :
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def bfs(v) :
    d = 0
    queue = deque([(v, d)])

    while queue :
        c, d = queue.popleft()
        if c == j :
            return d

        if not visited[c] :
            d += 1
            visited[c] = True

            for n in adj[c] :
                if not visited[n] :
                    queue.append((n, d))

    return -1

print(bfs(i))