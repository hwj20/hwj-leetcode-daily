'''
2441. Largest Positive Integer That Exists With Its Negative
Easy
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
'''


'''
思考是不是最优解
'''



class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        s = set(nums)

        for n in nums:
            if n > 0:
                break
            if (-n) in s:
                return -n

        return -1 