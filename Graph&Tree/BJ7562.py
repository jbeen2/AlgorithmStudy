from collections import deque

T = int(input())
for _ in range(T) :
    l = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())

    visited, dist = [[False]*l for _ in range(l)], [[0]*l for _ in range(l)]
    dx, dy = [1, -1, 1, -1, 2, 2, -2, -2], [2, 2, -2, -2, 1, -1, 1, -1]

    def bfs(i,j) :
        queue = deque([(i,j)])
        visited[i][j], dist[i][j] = True, 0

        while queue :
            m, n = queue.popleft()

            for k in range(8) :
                row = m + dx[k]
                col = n + dy[k]

                if (0 <= row < l) and (0 <= col < l) :
                    if not visited[row][col] :
                        queue.append((row, col))
                        visited[row][col] = True
                        dist[row][col] = dist[m][n] + 1

    bfs(a,b)
    print(dist[x][y])
