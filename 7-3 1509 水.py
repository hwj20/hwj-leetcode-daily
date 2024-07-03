'''
1509
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
'''

'''
困
'''
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) <= 4:
            return 0
        ans = nums[-1]-nums[0]

        for i in range(4):
            ans = min(nums[-1-(3-i)]-nums[i],ans)
        return ans
