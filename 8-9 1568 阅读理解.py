'''
1568
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.
'''

'''
not understanding the problemset，看了两天，我终于看懂题目了（绷）
''' 
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands():
            seen = set()
            
            def dfs(r, c):
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            stack.append((nx, ny))
            
            islands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in seen:
                        islands += 1
                        seen.add((i, j))
                        dfs(i, j)
            return islands
        
        if count_islands() != 1:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        
        return 2
