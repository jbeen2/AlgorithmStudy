# -*- coding: utf-8 -*-
from collections import deque

N, M = map(int, input().split())
adj = [[int(i) for i in str(input())] for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited, dist = [[False]*M for _ in range(N)], [[0]*M for _ in range(N)]  # bfs 에서는 방문 여부 설정해 줘야 함!

def bfs(x,y) :
    queue = deque([(x,y)])
    visited[x][y], dist[x][y] = True, 1

    while queue :
        a,b = queue.popleft()
        for i in range(4) :
            row = a + dx[i]
            col = b + dy[i]

            if (0 <= row < N) and (0 <= col < M):
                if not visited[row][col] and adj[row][col] == 1 :
                    queue.append((row, col))
                    visited[row][col] = True
                    dist[row][col] = dist[a][b] + 1


bfs(0,0)
print(dist[-1][-1])
