'''
179
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
'''

'''
6
'''
from functools import cmp_to_key

class Solution:
    def largestNumber(self,nums):
        # Convert integers to strings
        nums = list(map(str, nums))
        
        # Define custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        # Sort using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Handle the edge case where the largest number is "0"
        if nums[0] == '0':
            return '0'
        
        # Join the sorted list into a single string
        return ''.join(nums)        