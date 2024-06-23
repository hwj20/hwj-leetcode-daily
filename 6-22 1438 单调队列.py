'''
1438

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
'''

'''
单调队列经典题,手残，没写出来，heap吧...用了俩heap，还是觉得不对，看眼答案，其实这两个合起来就是正确答案了
'''


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        increase = deque()
        decrease = deque()
        max_length = 0
        left = 0

        for right in range(len(nums)):
            while increase and nums[right] < increase[-1]:
                increase.pop()
            increase.append(nums[right])
            
            while decrease and nums[right] > decrease[-1]:
                decrease.pop()
            decrease.append(nums[right])
            
            while decrease[0] - increase[0] > limit:
                if nums[left] == increase[0]:
                    increase.popleft()
                if nums[left] == decrease[0]:
                    decrease.popleft()
                left += 1
                
            max_length = max(max_length, right - left + 1)
        
        return max_length