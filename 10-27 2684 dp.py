'''
2684
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.
'''

'''
dp
'''

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans = 0
        dp = [[0]*n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                moved = False
                if j > 0 and grid[i][j-1] < grid[i][j]:
                    dp[i][j] = max(dp[i][j-1],dp[i][j])
                    if dp[i][j-1] != 0 or j == 1:
                        moved = True
                if j > 0 and i > 0 and grid[i-1][j-1] < grid[i][j]:
                    dp[i][j] = max(dp[i-1][j-1],dp[i][j])
                    if dp[i-1][j-1] != 0 or j == 1:
                        moved = True
                if j > 0 and i+1 < m and grid[i+1][j-1] < grid[i][j]:
                    dp[i][j] = max(dp[i+1][j-1],dp[i][j])
                    if dp[i+1][j-1] != 0 or j == 1:
                        moved = True
                if moved:
                    dp[i][j] += 1
                ans = max(ans,dp[i][j])
        # print(dp)
        return ans