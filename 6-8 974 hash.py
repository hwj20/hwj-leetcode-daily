'''
974. Subarray Sums Divisible by K
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
'''

'''
昨天的hash
'''


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        d,s = defaultdict(int),0
        ans = 0
        for i,n in enumerate(nums):
            s += n
            s %=  k
            if s == 0:
                ans += d[s]+1
                d[s] += 1
                continue
            else:
                ans += d[s]
                d[s] += 1
        return ans