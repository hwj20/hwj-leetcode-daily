'''
1380
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
'''

'''
50 的数据量，直接判断就是了
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                # print(matrix[i][j])
                flag = False
                for k in range(m):
                    if matrix[i][j] < matrix[k][j]:
                        flag = True
                        break
                if flag:
                    continue
                for l in range(n):
                    if matrix[i][j] > matrix[i][l]:
                        flag = True
                        break
                if flag:
                    continue
                ans.append(matrix[i][j])
        return ans

        