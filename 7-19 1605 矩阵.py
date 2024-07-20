'''
1605
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
'''

'''
毫无头绪，
看了个解，和我想得差不多，但我没有推出解的合理性，或者说后面的数学规律
'''


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c=len(rowSum), len(colSum)
        arr=[[0]*c for _ in range(r)]
        i, j=0, 0
        while i<r and j<c:
            x=min(rowSum[i], colSum[j])
            arr[i][j]=x
            rowSum[i]-=x
            colSum[j]-=x
            i+=(rowSum[i]==0)
            j+=(colSum[j]==0)
        return arr