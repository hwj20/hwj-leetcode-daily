'''
861. Score After Flipping Matrix
Medium
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).
'''


'''
对于列运算，只需要该列上的0比该列上的1多就赚了，对于行运算，只需要最高位是1就行了
你们怎么知道我打败了100%的python用户
'''



class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        for i in range(m):
            if grid[i][0] ==0:
                for j in range(n):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        ans = 0
        now = 1
        print(grid)
        # print(n-1)
        # print
        # print(range(n-1,-1 -1))
        for j in range(n-1,-1,-1):
            all_1 = 0
            for i in range(m):
                if grid[i][j] == 1:
                    all_1 += 1
            # print(all_1)
            ans += now*max(all_1,m-all_1)
            now <<= 1
        return ans