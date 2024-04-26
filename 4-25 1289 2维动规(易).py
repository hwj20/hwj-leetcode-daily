'''
1289. Minimum Falling Path Sum II
Hard

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.
'''

'''
这不经典动规题吗？值得hard？
可以用两个min来优化，从n^3变n^2，不过硬跑也能过...
'''


class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        ans = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(n):
            ans[0][i] = grid[0][i]
        for i in range(1,m):
            for j in range(n):
                mi = float('inf')
                for k in range(n):
                    if k == j:
                        continue
                    mi = min(mi,ans[i-1][k])
                ans[i][j] = mi + grid[i][j]
        # print(ans)
        return min(ans[m-1])