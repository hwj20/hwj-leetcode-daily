'''
330  Patching array
Hard
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.
'''

'''
对于第n的解，我们只需要保证n-1的解work，并且我们 有一个多余的小于n的item z 这样它可以加到 n-z这个组合里，否则我们就要召唤一个，显然，召唤n是最划算的，因为这会让解向右平移n格
'''

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        now_sum,idx = 0,0
        ans = 0
        i = 1
        while i < n+1:
            if idx < len(nums) and nums[idx] <= i:  # i = now_sum+1
                now_sum += nums[idx]
                idx += 1
            else:
                ans += 1
                now_sum += i
            i = now_sum + 1    
        return ans
