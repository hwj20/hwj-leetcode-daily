'''
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
'''

'''
相当于判断数组里有没有连续数组是k的整数倍，如果直接判断的话，时间复杂度是n^2，先试试，T了
看下答案，太美丽了
'''


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d,s = {0:-1},0
        for i,n in enumerate(nums):
            s = (s+n)%k
            if s not in d:
                d[s] = i
            else:
                if i-d[s] >= 2:
                    return True
        return False
        