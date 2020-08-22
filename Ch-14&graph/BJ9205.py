# 틀렸습니다
T = int(input())
for _ in range(T) :
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n+2)]
    distlst = []

    def dfs(lst) :
        queue = [lst[0], lst[1]]

        while len(lst) > 2 :
            dist = abs(queue[1][0] - queue[0][0]) + abs(queue[1][1] - queue[0][1])
            distlst.append(dist)

            lst.pop(0)
            dfs(lst)

    dfs(lst)

    dist = [d > 1000 for d in distlst]
    print("happy" if dist == ([False] * len(dist)) else "sad")

