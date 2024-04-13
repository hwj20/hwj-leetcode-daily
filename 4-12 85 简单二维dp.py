'''
85. Maximal Rectangle
Hard
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area
'''


'''
第一眼看数据量大小，好像搜索题; 搜索的话O((mn)^2)
有点困，就先看答案了，是dp题，看着答案突然想起来自己以前做过类似的哈哈哈
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m,n = len(matrix),len(matrix[0])
        ans = 0
        dp = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':
                    dp[(i,j)]=(0,0)
                else:
                    x = dp[(i,j-1)][0]+1 if j>0 else 1
                    y = dp[(i-1,j)][1]+1 if i>0 else 1
                    dp[(i,j)] = (x,y)
                    ans = max(x,y,ans)
                    minWidth = x
                    # verical max possible
                    for r in range(i-1,i-y,-1):
                        minWidth = min(minWidth,dp[(r,j)][0])
                        ans = max(ans,minWidth*(i-r+1))
        
        
        return ans