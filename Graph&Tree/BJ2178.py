N, M = map(int, input().split())
adj = []
for _ in range(N):
    n = str(input())
    adj.append([int(n[i]) for i in range(M)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]

def bfs(a,b) :
    visited[a][b] = True
    dist[a][b] = 1
    queue = [(a, b)]

    while queue :
        x, y = queue.pop(0)
        for i in range(4) :
            row = x + dx[i]
            col = y + dy[i]

            if (0 <= row < N) and (0 <= col < M):
                if not visited[row][col] and adj[row][col] == 1 :
                    queue.append((row, col))
                    dist[row][col] = dist[x][y] + 1
                    visited[row][col] = True

bfs(0,0)
print(dist[N-1][M-1])







