'''
995
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.
'''

'''
咋感觉做过这道题考虑边界情况
'''
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s  = deque()
        flip = 0
        ans = 0
        for i in range(len(nums)-k+1):
            if len(s) != 0 and s[0] == i:
                flip = flip ^ 1
                s.popleft()
            if nums[i] ^ flip == 0:
                flip = flip ^ 1
                ans += 1
                s.append(i+k)
        for i in range(len(nums)-k+1,len(nums)):
            if len(s) != 0 and s[0] == i:
                flip = flip ^ 1
                s.popleft()
            if nums[i] ^ flip == 0:
                return -1
        return ans            
