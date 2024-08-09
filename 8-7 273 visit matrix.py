'''
840
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

'''

'''
枚举矩阵
'''

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(x,y):
            # print('-')
            if x < 0 or x+2>= m or y < 0 or y+2 >= n:
                return False
            s = [0]*8
            sx = [0,1,2,0,0,0,0,0]
            sy = [0,0,0,0,1,2,0,2]
            dx = [0,0,0,1,1,1,1,1]
            dy = [1,1,1,0,0,0,1,-1]
            vis = set()
            for i in range(3):
                for j in range(3):
                    
                    if grid[x+i][y+j] in vis or grid[x+i][y+j] > 9 or grid[x+i][y+j]<1:
                        return False
                    vis.add(grid[x+i][y+j])
            for k in range(8):
                for i in range(3):
                    s[k] += grid[sx[k]+x][sy[k]+y]
                    sx[k] += dx[k]
                    sy[k] += dy[k]
                if k != 0 and s[k] != s[k-1]:
                    return False
            return True
        
        res = 0
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if is_magic(i,j):
                    res += 1
        return res