'''
2134
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.
'''

'''
sliding window
'''


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        l = sum(nums)
        n = len(nums)
        a = sum(nums[:l])
        ans = l-a
        for i in range(1,n):
            # print(a)
            if nums[i-1] == 1:
                a -= 1
            if nums[(i+l-1)%n] == 1:
                a += 1
            ans = min(ans, l-a)
        return ans 
