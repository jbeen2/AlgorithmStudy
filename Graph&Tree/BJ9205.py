# -*- coding: utf-8 -*-
# 1. 편의점과 도착지 좌표를 d에 저장
# 2. d안의 좌표를 하나씩 불러오면서 현재 위치와의 맨해튼 거리와 맥주양을 비교하여 이동가능한지 검사
# 3. bfs로 이동하면서 목표에 도착하면 happy 불가능하면 sad 출력

from collections import deque
def bfs(x,y):
    queue, current = deque(), []
    queue.append([x,y])
    current.append([x,y])

    while queue:
        i, j = queue.popleft()
        if i == x1 and j == y1 :
            return "happy"

        for nx,ny in loc :
            if [nx,ny] not in current :
                dist = abs(nx - i) + abs(ny - j)
                if dist <= 1000 :
                    queue.append([nx,ny])
                    current.append([nx, ny])
    return "sad"

T = int(input())
for _ in range(T) :
    n = int(input())
    x0, y0 = map(int, input().split())  # 상근이네 집
    loc = [list(map(int, input().split())) for _ in range(n)]  # 편의점 n
    x1, y1 = map(int, input().split())  # 페스티벌
    loc.append([x1,y1])

    print(bfs(x0,y0))