F, S, G, U, D = map(int, input().split())
visited = [False] * (F+1)

def bfs(F, S, G, U, D) :
    dist = 0
    queue = [[S,dist]]

    while queue :
        cur = queue.pop(0)
        dist = cur[1]

        if not visited[cur[0]] :
            visited[cur[0]] = True
            if cur[0] == G :
                return dist


            if cur[0]+U <= F and not visited[cur[0]+U]:
                queue.append([cur[0]+U, dist+1])

            if cur[0]-D > 0 and not visited[cur[0]-D]:
                queue.append([cur[0]-D, dist+1])


    return "use the stairs"



print(bfs(F, S, G, U, D))