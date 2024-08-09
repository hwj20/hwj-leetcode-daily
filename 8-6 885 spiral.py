'''
885
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.
'''

'''
painful
'''

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        dr = -1
        res = []
        vised = 0
        nx,ny = rStart,cStart
        vis = set()
        r,nr = 1,0
        while vised <= rows*cols:
            # print(nx,ny)
            vis.add((nx,ny))
            if 0<=nx<rows and 0 <= ny < cols:
                vised += 1
                res.append([nx,ny])
                if vised == rows*cols:
                    break
            dr += 1
            dr %= 4
            tx = nx + dx[dr]
            ty = ny + dy[dr]
            if (tx,ty) in vis:
                dr -= 1
                dr %= 4
            nx = nx + dx[dr]
            ny = ny + dy[dr]
            vis.add((nx,ny))

        return res
                
