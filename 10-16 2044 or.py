'''
2044
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
'''

'''
just or?
'''

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for n in nums:
            mx = mx | n
            # print(mx,n)
        # print(3 or 5)
        global ans
        ans = 0
        # print(mx)
        def dfs(idx,now):
            global ans
            if now == mx:
                print(idx,now,1 << (len(nums)-idx))
                ans += (1 << (len(nums)-idx))
                return
            if idx == len(nums):
                return
            dfs(idx+1,now)
            dfs(idx+1,now | nums[idx])
        dfs(0,0)
        return 