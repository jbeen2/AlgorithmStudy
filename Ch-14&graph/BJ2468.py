import sys
sys.setrecursionlimit(10**6)

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dist = []

def dfs(x,y,k) :
    visited[x][y] = True

    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]

        if (0 <= col < N) and (0 <= row < N) and adj[row][col] > k:
            if not visited[row][col] :
                dfs(row, col, k)


for k in range(max(max(adj))+1) :
    total = 0
    visited = [[False] * N for _ in range(N)]
    for v in range(N):
        for u in range(N):

            if not visited[v][u] and adj[v][u] > k:
                dfs(v, u, k)
                total += 1
    dist.append(total)

print(max(dist))




