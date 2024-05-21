'''
78. Subsets
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

'''
枚举题
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        vis = [False]*len(nums)
        # choose = [False]*len(nums)
        def dfs(now):
            if now == len(nums):
                ans = []
                for i in range(len(nums)):
                    if vis[i]:
                        ans.append(nums[i])
                res.append(ans)
                return
            dfs(now+1)
            vis[now] = True
            dfs(now+1)
            vis[now] = False
        dfs(0)
        # print(len(res))
        return res