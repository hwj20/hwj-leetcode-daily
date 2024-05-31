'''
260. Single Number III
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
'''

'''
经典二进制题，第一次全都xor，得俩数xor的结果，拿xor的结果再去and...不会了，看看解，这个mask seperate 太妙了
我好累啊，我想睡觉zzz
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x_res = 0
        for num in nums:
            x_res ^= num
        mask = x_res & -x_res
        num1, num2 = 0,0
        for num in nums:
            if num&mask != 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1,num2]
        