'''
2501
You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''


'''
double-exponential growth 
'''
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        s = set(nums)
        for i in nums:
            tmp = 1
            now = i
            while now*now in s:
                tmp += 1
                now = now*now
            ans = max(ans,tmp)

        return -1 if ans <= 1 else ans