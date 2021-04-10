from collections import deque
N, K = map(int, input().split())
visited = [False] * 100001

def bfs(v) :
    d = 0
    queue = deque([(v, d)])
    visited[v] = True

    print(queue)

    while queue :
        i, d = queue.popleft()
        print(i, d)

        if not visited[i] :
            visited[i] = True
            if i == K :
                return d

            d += 1
            if i-1 >= 0 :
                visited[i-1] = True
                queue.append((i-1, d))

            if i+1 <= 100000 :
                visited[i+1] = True
                queue.append((i+1, d))

            if i*2 <= 100000 :
                visited[i*2] = True
                queue.append((i*2, d))

    return d

print(bfs(N))

