# Not passed
def solution(n, computers):
    def dfs(x, y):
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        computers[x][y] = 0  # 방문 처리

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]

            if (0 <= col < n) and (0 <= row < n):
                if computers[row][col] == 1:
                    dfs(row, col)

    answer = 0
    for v in range(n):
        for u in range(n):
            if computers[v][u] == 1:
                dfs(v, u)  # dfs 로 방문할 수 있는 노드 다 방문하면
                answer += 1
    return answer

n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))