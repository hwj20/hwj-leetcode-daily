'''
2373. Largest Local Values in a Matrix
Easy

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix. 
'''


'''
简单题，n只有100，n^4的算法都能过，但是看答案有没有更快的方法...发现直接max比大部分算法都要快，乐
'''


class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """


        return [[max(max(grid[i][j:j+3]),max(grid[i+1][j:j+3]),max(grid[i+2][j:j+3])) for j in range(len(grid)-2)] for i in range(len(grid)-2)]

        n = len(grid)

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                temp = 0

                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        temp = max(temp, grid[k][l])

                grid[i - 1][j - 1] = temp

        n = len(grid)
        grid = [row[:n-2] for row in grid[:n-2]]

        return grid        