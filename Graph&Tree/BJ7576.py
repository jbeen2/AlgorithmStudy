import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
adj = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
que = deque([(i,j) for j in range(M) for i in range(N) if adj[i][j]==1])

def bfs() :
    while que :
        a, b = que.popleft()
        for i in range(4) :
            row = a + dx[i] ; col = b + dy[i]
            if (0<=row<N) and (0<=col<M) and adj[row][col] == 0 :
                    que.append((row, col))
                    adj[row][col] = adj[a][b] + 1

bfs()
answ = 0
for i in adj :
    for j in i :
        if j==0:
            print(-1)
            exit(0)
    answ = max(answ,max(i))
print(answ-1)