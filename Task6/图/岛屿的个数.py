class Solution:
    def numIslands(self, grid):

        def bfs(grid, i, j, m, n):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return

            grid[i][j] = 2
            bfs(grid, i + 1, j, m, n)
            bfs(grid, i - 1, j, m, n)
            bfs(grid, i, j + 1, m, n)
            bfs(grid, i, j - 1, m, n)

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    bfs(grid, i, j, m, n)
        return res