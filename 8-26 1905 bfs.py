'''
1905
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
'''

'''
bfs
'''
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # type: 1 (1 1) 2(1 0)-found exclude (0 1) pass (0 0) ignore 
        # directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # def find(x,y):
        #     to_vis = [(x,y)]
        #     vised = set()
        #     found = False
        #     not_included = False
        #     if grid1[x][y] == 0:
        #         not_included = True
        #     while to_vis:
        #         cx,cy = to_vis.pop()
        #         grid2[cx][cy] = -1
        #         vised.add((cx,cy))
        #         for dx,dy in directions:
        #             nx,ny = cx+dx,cy+dy
        #             if 0<=nx<len(grid1) and 0<=ny<len(grid1[0]):
        #                 if grid2[nx][ny] == 1:
        #                     if grid1[nx][ny] == 0:
        #                         not_included = True
        #                     if (nx,ny) not in vised:
        #                         to_vis.append((nx,ny))
        #                 else:
        #                     if grid1[nx][ny] == 1:
        #                         found = True
        #     if not_included:
        #         return False
        #     return found
        # ans = 0
        # for i in range(len(grid1)):
        #     for j in range(len(grid1[0])):
        #         if grid2[i][j] == 1:
        #             res = find(i,j)
        #             if res:
        #                 print(i,j)
        #                 ans += 1
        # return ans    
        # Directions for BFS traversal (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(x, y):
            # Initialize BFS queue and visited set
            to_vis = [(x, y)]
            vised = set()
            vised.add((x, y))
            is_sub_island = True
            if grid1[x][y] == 0:
                is_sub_island = False
            
            # BFS loop
            while to_vis:
                cx, cy = to_vis.pop(0)  # FIFO order
                grid2[cx][cy] = -1  # Mark the cell as visited
                
                # Check each direction
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    
                    # Boundary check
                    if 0 <= nx < len(grid1) and 0 <= ny < len(grid1[0]):
                        # If the neighboring cell in grid2 is land
                        if grid2[nx][ny] == 1:
                            # Check if the corresponding cell in grid1 is water
                            if grid1[nx][ny] == 0:
                                is_sub_island = False
                            
                            if (nx, ny) not in vised:
                                vised.add((nx, ny))
                                to_vis.append((nx, ny))
            
            # Return whether the current island in grid2 is a sub-island
            return is_sub_island
        
        # Main loop over all cells
        ans = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                # Start BFS if the cell is land in grid2
                if grid2[i][j] == 1:
                    if bfs(i, j):
                        # print(i,j)
                        ans += 1
        
        return ans                    
            
