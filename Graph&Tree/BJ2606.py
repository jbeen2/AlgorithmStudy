from collections import deque

N, M = int(input()), int(input())
adj = [[] for _ in range(N+1)]
visited1, visited2 = [False] * (N+1), [False] * (N+1)
dfs_list, bfs_list = [], []

for _ in range(M) :
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(v) :
    visited1[v] = True
    dfs_list.append(v)

    for i in adj[v] :
        if not visited1[i] :
            dfs(i)

dfs(1)
print(len(dfs_list)-1)


def bfs(v) :
    queue = deque([v])
    visited2[v] = True

    while queue :
        n = queue.popleft()
        bfs_list.append(n)

        for e in adj[n] :
            if not visited2[e] and n not in queue :
                queue.append(e)
                visited2[e] = True

bfs(1)
print(len(bfs_list)-1)
