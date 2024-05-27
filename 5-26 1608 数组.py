'''
1608
Easy
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
'''


'''
简单题，有点脑筋急转弯的意思
'''


class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= len(nums)-i:
                if i > 0 and nums[i-1] >= len(nums)-i:
                    continue
                return len(nums)-i
        return -1