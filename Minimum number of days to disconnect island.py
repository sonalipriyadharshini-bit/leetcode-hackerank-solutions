class Solution:
    def minDays(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 0 or (i, j) in visited:
                return
            
            visited.add((i, j))
            dfs(i+1, j, visited)
            dfs(i-1, j, visited)
            dfs(i, j+1, visited)
            dfs(i, j-1, visited)

        def count_islands():
            visited = set()
            count = 0
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j, visited)
                        count += 1
            return count

        # Step 1: check initial state
        if count_islands() != 1:
            return 0

        # Step 2: try removing one land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        grid[i][j] = 1
                        return 1
                    grid[i][j] = 1

        # Step 3: fallback
        return 2
