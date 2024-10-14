'''
2530
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.
'''

'''
greedy
'''

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        ans = 0
        nums = [float(-x) for x in nums]
        heapq.heapify(nums)
        while k > 0:
            head = heapq.heappop(nums)
            ans += (-head)
            # print(-head)
            # print(-ceil(-head / 3))
            heapq.heappush(nums,-ceil(-head / 3))
            k -= 1
        return int(ans)