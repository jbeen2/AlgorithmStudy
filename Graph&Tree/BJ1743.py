import sys
sys.setrecursionlimit(10**6)

N, M, K = map(int, sys.stdin.readline().split())
adj = [[0]*M for _ in range(N)]
for _ in range(K) :
    r, c = map(int, sys.stdin.readline().split())
    adj[r-1][c-1] = 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def dfs(x,y,dist) :
    adj[x][y] = 0
    for i in range(4) :
        row = x + dx[i] ; col = y + dy[i]
        if (0<=col<M) and (0<=row<N) :
            if adj[row][col] == 1 :
                dist = dfs(row,col,dist+1)
    return dist

answer = []
for v in range(N) :
    for u in range(M) :
        if adj[v][u] == 1 :
            answer.append(dfs(v,u,1))

print(max(answer))