N, K = map(int, input().split())
visited = [False] * 100001

def bfs(N) :
    dist = 0
    queue = [[N,dist]]

    while queue :
        cur = queue.pop(0)
        dist = cur[1]

        if not visited[cur[0]] :
            visited[cur[0]] = True
            if cur[0] == K :
                return dist

            dist += 1
            if cur[0]+1 <= 100000 :
                queue.append([cur[0]+1, dist])
            if cur[0]-1 >= 0 :
                queue.append([cur[0]-1, dist])
            if cur[0]*2 <= 100000 :
                queue.append([cur[0]*2, dist])

    return dist

print(bfs(N))