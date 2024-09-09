'''
2326
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.
'''


'''
这个螺旋怎么还有IV
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        global d
        dr = [(0,1),(1,0),(0,-1),(-1,0)]
        d = 0
        mat = [[-1]*n for _ in range(m)]
        def vis(now,x,y):
            # print(x,y)
            global d
            if now == None:
                return
            mat[x][y] = now.val
            if now.next == None:
                return
            dx,dy = dr[d]
            nx = x+dx
            ny = y+dy
            while nx<0 or nx>=m or ny<0 or ny>=n or mat[nx][ny] != -1:
                # print(nx,ny)
                d +=1
                d %=4
                dx,dy = dr[d]                
                nx = x+dx
                ny = y+dy
            vis(now.next,nx,ny)
        vis(head,0,0)
        return mat
