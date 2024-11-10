'''
1829
You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:

Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
Remove the last element from the current array nums.
Return an array answer, where answer[i] is the answer to the ith query.
'''

'''

'''

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        t = 0
        # tmp = []
        ans = []
        for n in nums:
            t = t ^ n
            i = 0
            now = 0
            tmp = t
            # mx = 1 << maximumBit
            idx = 1
            while i < maximumBit:
                if tmp & idx == 0:
                    now = now | idx
                i += 1
                idx <<= 1
            # now -= mx
            ans.insert(0,now)
        return ans