T = int(input())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(T) :
    M, N, K = map(int, input().split())
    adj = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K) :
        u, v = map(int, input().split())
        adj[v][u] = 1

    def dfs(x,y) :
        adj[x][y] = 0

        for i in range(4) :
            row = x + dx[i]
            col = y + dy[i]

            if (0 <= col < M) and (0 <= row < N) :
                if adj[row][col] == 1 :
                    dfs(row, col)

    for v in range(N) :
        for u in range(M) :
            if adj[v][u] == 1 :
                dfs(v, u)
                count += 1

    print(count)


