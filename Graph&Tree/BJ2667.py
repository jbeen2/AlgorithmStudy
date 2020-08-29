import sys
sys.setrecursionlimit(10**6)

N = int(input())
adj = []
for _ in range(N):
    n = str(input())
    adj.append([int(n[i]) for i in range(N)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
total = 0
dist = []

def dfs(x,y,d) :
    adj[x][y] = 0

    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]

        if (0 <= col < N) and (0 <= row < N):
            if adj[row][col] == 1 :
                dfs(row, col, d)

    dist.append(d)

for v in range(N) :
    for u in range(N) :
        if adj[v][u] == 1 :
            dfs(v,u,total)
            total += 1

final = sorted([dist.count(i) for i in range(max(dist)+1)])

print(total)
for f in final :
    print(f)