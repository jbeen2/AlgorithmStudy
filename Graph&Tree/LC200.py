from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        total = 0

        def dfs(x, y):
            grid[x][y] = 0

            for i in range(4):
                row = x + dx[i]
                col = y + dy[i]

                if (0 <= col < len(grid[0])) and (0 <= row < len(grid)):
                    if grid[row][col] == "1":
                        dfs(row, col)

        for v in range(len(grid)):
            for u in range(len(grid[0])):
                if grid[v][u] == "1":
                    dfs(v, u)
                    total += 1

        return total