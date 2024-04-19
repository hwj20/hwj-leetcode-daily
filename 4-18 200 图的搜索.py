'''
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''


'''
这个才是真的搜索题，昨天是我傻x了
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        drs = [(-1,0),(1,0),(0,1),(0,-1)]
        vis = set()
        m,n = len(grid),len(grid[0])
        def dfs(x,y):
            # print(x,y)
            vis.add((x,y))
            for dr in drs:
                dx,dy = dr[0],dr[1]
                nx,ny= x+dx,y+dy
                if not( nx < 0 or nx >= m or ny < 0 or ny >= n):
                    if grid[nx][ny] == '1':
                        if (nx,ny) not in vis:
                            dfs(nx,ny)
        ans = 0
        for sx in range(m):
            for sy in range(n):
                if grid[sx][sy] == '1' and (sx,sy) not in vis:
                    ans += 1
                    dfs(sx,sy)
        return ans