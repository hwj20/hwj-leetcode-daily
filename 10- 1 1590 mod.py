'''
1590
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.
'''


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        s = [0]*(n+1)
        k = sum(nums)%p
        if k == 0:
            return 0
        for i in range(n):
            s[i+1] = s[i]+nums[i]
            s[i+1]%= p
            if nums[i]%p == k:
                return 1
        ans = float('inf')

        m = {}
        for i in range(n+1):
            target = k-s[i]
            m[-s[i]] = m[p-s[i]] = i
            # print(m,target)
            if target in m:
                ans = min(ans,i-m[target])
            # print(m)
        return  -1 if ans == n else ans
