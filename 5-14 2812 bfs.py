'''
2812. Find the Safest Path in a Grid
Medium
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.
'''

'''
这题啥意思啊，就是说找一条路，然后隔有1的格子最远，我们只需要计算每个格子的safeness factor，然后找最高的路径，
上头了，从递推写到算最短路径，凭什么bfs能过，而我枚举不能过
'''

class Solution(object):
    import copy

    def bfs(self, grid, score, n):
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    score[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            s = score[x][y]

            dr = set([(0,1),(-1,0),(1,0),(0,-1)])

            for d in dr:
                dx,dy = d[0],d[1]
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < n and 0 <= new_y < n and score[new_x][new_y] > s + 1:
                    score[new_x][new_y] = s + 1
                    q.append((new_x, new_y))


    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        t_cells = set()
        n = len(grid)
        # for i in range(n):
        #     for  j in range(n):
        #         if grid[i][j] == 1:
        #             t_cells.add((i,j))
        # if len(t_cells) == 0:
        #     return 0
        safe_f = [[float('inf')]*n for _ in range(n)]
        self.bfs(grid,safe_f,n)
        # for i in range(n):
        #     for  j in range(n):
        #         # if grid[i][j] == 0:
        #         for t_cell in t_cells:
        #             safe_f[i][j] = min(safe_f[i][j],abs(t_cell[0]-i)+abs(t_cell[1]-j))
        # ans = copy.deepcopy(safe_f)
        # print(safe_f)
        # ans[0][0] = safe_f[0][0]
        # for i in range(n):
        #     for  j in range(n):
        #         ans[i][j] = max(-1 if j-1 <0 else ans[i][j-1],-1 if i-1 < 0 else ans[i-1][j]
        #         )
        #         if ans[i][j] == -1:
        #             ans[i][j] =  safe_f[i][j]
        #         ans[i][j] = min(ans[i][j],safe_f[i][j])

        # now_ans = ans[n-1][n-1]

        # for j in range(n):
        #     for  i in range(n):
        #         ans[i][j] = max(-1 if j-1 <0 else ans[i][j-1],-1 if i-1 < 0 else ans[i-1][j],
        #         -1 if j+1>=n else ans[i][j+1],-1 if i+1 >= n else ans[i+1][j]
        #         )
        #         if ans[i][j] == -1:
        #             ans[i][j] =  safe_f[i][j]
        #         ans[i][j] = min(ans[i][j],safe_f[i][j])

        # to_vis = set([(0,0)])
        dr = set([(0,1),(-1,0),(1,0),(0,-1)])
        vis = [[False]*n for _ in range(n)]
        # print(safe_f)
        pq = [(-safe_f[0][0], 0, 0)]
        heapq.heapify(pq)        
        while pq:
            now,x,y = heapq.heappop(pq)
            if x == n-1 and y == n-1:
                return -now
            for d in dr:
                dx,dy = d[0],d[1]
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and not vis[nx][ny]:
                    s  = min(-now,safe_f[nx][ny])
                    heapq.heappush(pq,(-s,nx,ny))
                    vis[nx][ny] = True
        # print(ans)
        # return  ans[n-1][n-1]