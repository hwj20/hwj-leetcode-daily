'''
1863. Sum of All Subset XOR Totals
Easy

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
'''

'''
数量级只有12,2的12次方的时间复杂度，直接枚举就行了
'''


class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # vis = set()
        ans = [0]
        def dfs(now,val):
            # vis.add(now)

            if now == len(nums):
                ans[0] += val
                return
            num = nums[now]
            dfs(now+1,val ^ num)
            dfs(now+1,val)
        dfs(0,0)
        return ans[0]


            