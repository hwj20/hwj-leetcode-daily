'''
1508
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
'''

'''
sliding window
'''

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        mod = int(1e9+7)
        for i in range(n):
            s = nums[i]
            arr.append(s)
            for j in range(i+1,n):
                s += nums[j]
                s %=mod
                arr.append(s)
        arr.sort()
        return sum(arr[left-1:right])%mod
