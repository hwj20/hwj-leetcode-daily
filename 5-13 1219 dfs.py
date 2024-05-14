'''
1219. Path with Maximum Gold
Medium
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
'''

'''
dfs, 没什么好说的，但我今天面试挂了，好难过啊，让我 push gpt 写个最快的算法
'''


class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(x, y, current_gold):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return current_gold
            
            # Collect the gold at the current cell
            gold_here = grid[x][y]
            grid[x][y] = 0  # Mark this cell as visited by setting it to 0
            max_gold = 0  # Track the maximum gold collected from this path

            # Explore the four possible directions
            max_gold = max(max_gold, dfs(x + 1, y, current_gold + gold_here))
            max_gold = max(max_gold, dfs(x - 1, y, current_gold + gold_here))
            max_gold = max(max_gold, dfs(x, y + 1, current_gold + gold_here))
            max_gold = max(max_gold, dfs(x, y - 1, current_gold + gold_here))
            
            # Backtrack: unmark the cell by restoring its original value
            grid[x][y] = gold_here
            
            return max_gold
        
        max_gold_collected = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    # Start DFS if there's gold in the cell
                    max_gold_collected = max(max_gold_collected, dfs(i, j, 0))
        
        return max_gold_collected
            