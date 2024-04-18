'''
463. Island Perimeter
Easy

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''

'''
今天心情不好，就随便写个搜索吧，这题真的是简单题吗，咋感觉简单题里没有图的遍历这种东西啊
'''

'''
看了眼标准答案，说只要判断两个格子之间有没有边就行了，6
'''


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        drs = [(-1,0),(1,0),(0,1),(0,-1)]
        vis = set()
        ans = [0]
        l,r = len(grid),len(grid[0])
        sx,sy = -1,-1
        for i in range(l):
            for j in range(r):
                if grid[i][j] == 1:
                    sx = i
                    sy = j
                    break
        if sx == -1: # no island found
            return 0

        def dfs(x,y):
            # print(x,y)
            vis.add((x,y))
            for dr in drs:
                dx,dy = dr[0],dr[1]
                nx,ny= x+dx,y+dy
                if not( nx < 0 or nx >= l or ny < 0 or ny >= r):
                    if grid[nx][ny]:
                        if (nx,ny) not in vis:
                            dfs(nx,ny)
                    else:
                        ans[0] += 1
                else:
                    ans[0] += 1
        dfs(sx,sy)
        return ans[0]
