import sys
sys.setrecursionlimit(10**6)

def dfs(v, G, visited, result) :
    visited[v] = True
    for node in G[v] :
        if not visited[node] :
            result.append(node)
            dfs(node, G, visited, result)
    result.append(v)

def reverse_dfs(v, G, visited, result) :
    visited[v] = True
    result.append(v)
    for node in G[v] :
        if not visited[node] :
            reverse_dfs(node, G, visited, result)

V, E = map(int, input().split())
adj, adj_T = [[] for _ in range(V+1)], [[] for _ in range(V+1)]
visited1, visited2 = [False] * (V + 1), [False] * (V + 1)

for _ in range(E) :
    a, b = map(int, input().split())
    adj[a].append(b)
    adj_T[b].append(a)

stack, scc = [], []
for k in range(1, V+1) :
    if not visited1[k] :
        dfs(k, adj, visited1, stack)

while stack :
    tmp = []
    node = stack.pop()
    if not visited2[node] :
        reverse_dfs(node, adj_T, visited2, tmp)
        scc.append(sorted(tmp))

print(len(scc))
for s in sorted(scc) :
    print(*s, -1)


# -*- coding: utf-8 -*-
# Memory Exceed...... ^_^ 인접 행렬로 풀어서 그런 것 같음

# def dfs(v, G, visited, result) :
#     visited[v] = True
#     result.append(v)
#     for w in range(V+1) :
#         if not visited[w] and G[v][w] == 1 :
#             dfs(w, G, visited, result)
#
# V, E = map(int, input().split())
# adj, adj_T = [[0] * (V + 1) for _ in range(V + 1)], [[0] * (V + 1) for _ in range(V + 1)]
# for _ in range(E) :
#     i, j = map(int, input().split())
#     adj[i][j] = 1
#     adj_T[j][i] = 1
#
# adj_result, adj_T_result = [], []
# for k in range(V+1) :
#     visited1, visited2 = [False] * (V + 1), [False] * (V + 1)
#     result1, result2 = [], []
#
#     dfs(k, adj, visited1, result1)
#     dfs(k, adj_T, visited2, result2)
#
#     adj_result.append(result1)
#     adj_T_result.append(result2)
#
# answer = []
# for a, b in zip(adj_result, adj_T_result) :
#     if len(a) == 1 :
#         answer.append(a)
#     else :
#         intersect = list(set(a) & set(b))
#         answer.append(intersect)
#
# answer_new = []
# for v in answer:
#     if v not in answer_new:
#         answer_new.append(v)
#
# answer_new.pop(0)
# print(len(answer_new))
# for a in answer_new :
#     print(*sorted(a), -1)