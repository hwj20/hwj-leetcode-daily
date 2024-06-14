'''
945. Minimum Increment to Make Array Unique
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.
'''


'''
sort 一遍比较就是了，比较简单
'''


class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        last = -1
        ans = 0
        for n in nums:
            if n <= last:
                ans += last+1-n
                last += 1
            else:
                last = n
        return ans