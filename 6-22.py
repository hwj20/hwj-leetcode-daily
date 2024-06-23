'''
1248
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
'''

'''
双指针;错啦错啦，没看样例，直接sum(xor1)-k就完啦;也不对...真头疼捏
'''

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # l,r = 0,0
        # ans = 0
        # while l < len(nums) and r < len(nums):
        #     # print(l,r)
        #     while  l < len(nums) and nums[l]%2 != 1:
        #         l += 1
        #     r = l 
        #     while r < len(nums) and r-l+1 < k :
        #         if nums[r]%2 == 1:
        #             r += 1
        #         else:
        #             break
        #     while r < len(nums) and r-l+1 == k:
        #         print(l,r)
        #         ans += 1
        #         if nums[r]%2 == 1:
        #             r += 1
        #             l += 1
        #         else:
        #             break
        #     l = r+1        
        # return sum([n%2 for n in nums])-k+1             
        pos = []
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                pos.append(i)
        ans = 0
        for i in range(len(pos)-k+1):
            l,r = pos[i], pos[i+k-1]
            l_0 = -1 if i == 0 else pos[i-1]
            l_a = l-l_0-1
            r_0 = len(nums) if i+k-1 == len(pos)-1 else pos[i+k]
            r_a = r_0-r-1
            ans += (l_a+1)*(r_a+1)
        return ans
                