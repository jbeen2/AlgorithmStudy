import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, sys.stdin.readline().split())
adj = [[1]*N for _ in range(M)]
for _ in range(K) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            adj[i][j] = 0

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
count, answer = 0, []
def dfs(x,y,d) :
    adj[x][y] = 0
    for i in range(4) :
        row = x + dx[i]
        col = y + dy[i]
        if (0<=col<N) and (0<=row<M) :
            if adj[row][col] == 1 :
                dfs(row,col,d)
    answer.append(d)

for v in range(M) :
    for u in range(N) :
        if adj[v][u] == 1 :
            dfs(v,u,count)
            count += 1

a = sorted([answer.count(i) for i in range(count)])
print(count)
print(*a)
