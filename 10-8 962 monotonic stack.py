'''
962
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
'''


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        stack = []
        
        # Step 1: Fill the stack with indices of a decreasing sequence
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # Step 2: Traverse from the end to the beginning to find the max width ramp
        max_width = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width