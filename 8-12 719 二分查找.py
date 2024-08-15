'''
719
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
'''

'''
try violence
为什么这个可以二分查找过啊
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        low, high = 0, nums[-1] - nums[0]

        def count_pairs(max_distance):
            count, j = 0, 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= max_distance:
                    j += 1
                count += j - i - 1
            return count

        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low