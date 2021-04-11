from collections import deque
N, K = map(int, input().split())
visited = [False] * 100001

def bfs(v) :
    d = 0
    queue = deque([(v, d)])

    while queue :
        i, d = queue.popleft()

        if not visited[i] :
            visited[i] = True
            if i == K :
                return d

            d += 1
            if i-1 >= 0 :
                queue.append((i-1, d))

            if i+1 <= 100000 :
                queue.append((i+1, d))

            if i*2 <= 100000 :
                queue.append((i*2, d))

    return d

print(bfs(N))

