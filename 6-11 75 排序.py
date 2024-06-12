'''
75. Sort Colors
Medium
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''


'''
桶排序; 或者快排
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(nums)-1
        while l < r:
            while nums[l] == 0:
                l += 1
                if l >= len(nums):
                    break
            while nums[r] == 2:
                r -= 1
                if r < 0:
                    break
            flag = False
            for j in range(l,r+1):
                if nums[j] == 0:
                    nums[j],nums[l] = nums[l],nums[j]
                    flag = True
                    break
                if nums[j] == 2:
                    nums[j],nums[r] = nums[r],nums[j]
                    flag = True
                    break      
            if not flag:
                break             
        return nums