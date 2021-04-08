# -*- coding: utf-8 -*-
from collections import deque

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]  # node 개수만큼 인접행렬 생성 (+1 : 1부터 시작하기 위해..)
adj = [sorted(a) for a in adj]  # 정렬

visited1, visited2 = [False] * (N+1), [False] * (N+1)     # 방문 list
dfs_list, bfs_list = [], []


# graph edge 연결 정보 담긴 adj matrix 생성
for _ in range(M) :
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


# dfs : stack & 재귀함수!
def dfs(current) :
    visited1[current] = True        # 현재 node 방문 처리
    dfs_list.append(current)

    for node in adj[current] :      # node 에 연결되어 있는 다른 node 에 대하여
        if not visited1[node] :     # 방문 안 했으면
            dfs(node)               # 재귀함수!


# bfs : queue & deque()
def bfs(root) :
    queue = deque([root])
    visited2[root] = True           # 현재 root 방문 처리

    while queue :                   # queue 가 empty 될 때 까지 반복
        current = queue.popleft()
        bfs_list.append(current)

        for node in adj[current] :
            if not visited2[node] and current not in queue :
                queue.append(node)  # node 에 연결되어 있는 방문하지 않은 node 삽입
                visited2[node] = True


dfs(V)
bfs(V)

print(*dfs_list)                    # list 안에 있는 값 바로 출력!
print(*bfs_list)