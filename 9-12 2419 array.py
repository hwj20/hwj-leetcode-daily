'''
2419
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.
'''

'''
and is a decreasing operation
'''




class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        ans = 1
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == m:
                cnt += 1
            else:
                cnt = 0
            ans = max(cnt,ans)
        return ans