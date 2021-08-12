import sys
sys.setrecursionlimit(10**6)
dx, dy = [1, -1, 0, 0, 1, -1, 1, -1], [0, 0, 1, -1, 1, 1, -1, -1]

def dfs(x,y) :
    adj[x][y] = 0   # 방문 처리
    for i in range(8) :
        row = x + dx[i]
        col = y + dy[i]
        if (0 <= col < w) and (0 <= row < h) :
            if adj[row][col] == 1 :
                dfs(row, col)

def solution(w,h,adj) :
    count = 0
    for v in range(h) :
        for u in range(w) :
            if adj[v][u] == 1 :
                dfs(v, u)
                count += 1
    return count

while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    adj = [[int(i) for i in sys.stdin.readline().split()] for _ in range(h)]
    print(solution(w,h,adj))
