'''
1937
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
'''


'''
看起来像dp，但是dp过不了这个数量级啊，让GPT教教我
'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev_dp = points[0][:]  # 初始化第一行的dp
        
        for i in range(1, m):
            left_max = [0] * n  # 从左到右的最大值
            right_max = [0] * n  # 从右到左的最大值
            curr_dp = [0] * n  # 当前行的dp
            
            # 从左到右计算每个位置的最大值
            left_max[0] = prev_dp[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j - 1] - 1, prev_dp[j])
            
            # 从右到左计算每个位置的最大值
            right_max[-1] = prev_dp[-1]
            for j in range(n - 2, -1, -1):
                right_max[j] = max(right_max[j + 1] - 1, prev_dp[j])
            
            # 计算当前行的dp
            for j in range(n):
                curr_dp[j] = points[i][j] + max(left_max[j], right_max[j])
            
            # 更新prev_dp为当前行的dp
            prev_dp = curr_dp[:]
        
        return max(prev_dp)