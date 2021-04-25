# -*- coding: utf-8 -*-
# 시간 초과 ...

import sys
sys.setrecursionlimit(10**6)

def dfs(v, G, visited, result) :
    visited[v] = True
    for node in G[v] :
        if not visited[node] :
            dfs(node, G, visited, result)
    result.append(v)

T = int(input())
for _ in range(T) :
    n = int(input())
    students = list(map(int, input().split()))
    adj, adj_T = [[] for _ in range(n+1)], [[] for _ in range(n+1)]
    visited1, visited2 = [False] * (n+1), [False] * (n+1)

    for i,j in enumerate(students) :
        adj[i+1].append(j)
        adj_T[j].append(i+1)

    stack, scc = [], []
    for k in range(1, n+1):
        if not visited1[k]:
            dfs(k, adj, visited1, stack)

    while stack:
        tmp = []
        node = stack.pop()

        if not visited2[node]:
            dfs(node, adj_T, visited2, tmp)
        scc.append(tmp)

    answer = []
    for s in scc :
        if len(s) == 1 :
            if s in adj and adj[s[0]] == s :
                answer.extend(s)
        else :
            answer.extend(s)

    print(n - len(answer))


# SCC (Strongly Connected Components) : Out(v).intersection(In(v))
# 1. SCC 그룹의 요소가 둘 이상이다.
# 2. SCC 그룹의 요소가 하나이고, 그 하나의 요소가 자기 자신을 가리키고 있으면 팀이 될 수 있다.

# 메모리 초과 : 인접 행렬 (2차원 배열)로 풀고 + 역방향 체크할 때 모든 노드에 대해 다시 돌면 메모리 초과 나는 듯..

# def dfs(v, G, visited, result) :
#     visited[v] = True
#     result.append(v)
#     for w in range(n+1) :
#         if not visited[w] and G[v][w] == 1 :
#             dfs(w, G, visited, result)
#
# T = int(input())
# for _ in range(T) :
#     n = int(input())
#     students = list(map(int, input().split()))
#
#     adj, adj_T = [[0]*(n+1) for _ in range(n+1)], [[0]*(n+1) for _ in range(n+1)]
#     for i,j in enumerate(students) :
#         adj[i+1][j] = 1
#         adj_T[j][i+1] = 1
#
#     adj_result, adj_T_result = [], []
#     for k in range(n+1) :
#         visited1, visited2 = [False] * (n + 1), [False] * (n + 1)
#         result1, result2 = [], []
#
#
#         dfs(k, adj, visited1, result1)
#         adj_result.append(result1)
#
#         result4 = result1.copy()
#         while result4 :
#             node = result4.pop()
#             result3 = []
#
#             if not visited2[node] :
#                 dfs(k, adj_T, visited2, result3)
#             result2.extend(result3)
#
#
#         adj_T_result.append(result2)
#
#     print(adj_result)
#     print(adj_T_result)
#
#
#     answer = []
#     for a, b in zip(adj_result, adj_T_result) :
#         if len(a) == 1 :
#             answer.extend(a)
#         else :
#             intersect = list(set(a) & set(b))
#             if not len(intersect) == 1 :
#                 answer.extend(intersect)
#
#     answer = list(set(answer))
#     print(n-len(answer)+1)