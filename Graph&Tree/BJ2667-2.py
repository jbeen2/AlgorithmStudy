# -*- coding: utf-8 -*-
N = int(input())
adj = [[int(i) for i in str(input())] for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

house, dist = 0, []
def dfs(x,y,d) :
    adj[x][y] = 0   # 방문 처리

    for i in range(4) :
        row = x + dx[i]
        col = y + dy[i]

        if (0 <= col < N) and (0 <= row < N) :
            if adj[row][col] == 1 :
                dfs(row, col, d)

    dist.append(d)

for v in range(N) :
    for u in range(N) :
        if adj[v][u] == 1 :
            dfs(v, u, house)   # dfs 로 방문할 수 있는 노드 다 방문하면
            house += 1         # 단지명 바꿔주기!

a = sorted([dist.count(i) for i in range(house)])

print(house)
print(*a, sep="\n")
