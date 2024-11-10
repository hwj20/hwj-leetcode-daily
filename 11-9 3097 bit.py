'''
3097
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty 
subarray of nums, or return -1 if no special subarray exists.
'''

'''
n^2 but pass?
'''
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bitCount = [0] * 32
        currentOR = 0
        left = 0
        minLength = float('inf')
        
        for right in range(n):
            currentOR |= nums[right]
            
            for bit in range(32):
                if nums[right] & (1 << bit):
                    bitCount[bit] += 1
            
            while left <= right and currentOR >= k:
                minLength = min(minLength, right - left + 1)
                
                updatedOR = 0
                for bit in range(32):
                    if nums[left] & (1 << bit):
                        bitCount[bit] -= 1
                    if bitCount[bit] > 0:
                        updatedOR |= (1 << bit)
                
                currentOR = updatedOR
                left += 1
        
        return minLength if minLength != float('inf') else -1        