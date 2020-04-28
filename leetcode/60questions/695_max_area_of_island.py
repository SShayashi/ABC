from typing import List


class Solution:
    count = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width, height = len(grid[0]), len(grid)
        g = [[[] for _ in range(width)] for _ in range(height)]
        for x in range(width):
            for y in range(height):
                if grid[y][x] == 0:
                    continue
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # +1, +1は斜めですよ．．．
                    nx = min(max(x + i, 0), width - 1)
                    ny = min(max(y + j, 0), height - 1)
                    if nx == x and ny == y:
                        continue
                    if grid[ny][nx] == 0:
                        continue
                    g[y][x].append((ny, nx))
        visited = []

        def dfs(islands):
            for y, x in islands:
                if (y, x) in visited:
                    continue
                visited.append((y, x))
                self.count += 1
                dfs(g[y][x])

        ans = 0
        for x in range(width):
            for y in range(height):
                if not g[y][x]:
                    continue
                if (y, x) in visited:
                    continue
                visited.append((y, x))
                self.count = 1
                dfs(g[y][x])
                ans = max(ans, self.count)
        if ans == 0:
            for i in range(width):
                for j in range(height):
                    if grid[j][i] == 1:
                        return 1
            return 0
        return ans

inputs = [[0,0]]
a = Solution().maxAreaOfIsland(inputs)
print(a)
