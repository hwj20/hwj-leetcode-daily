'''
2191
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Notes:

Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
'''

'''
又是个sort题目，没什么难度
'''


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def val(x):
            # print(x)
            if x == 0:
                return mapping[x]
            res = 0
            base = 1
            while x != 0:
                res = res+mapping[x%10]*base
                x //= 10
                base *= 10
            # print(res)
            return res
        return sorted(nums, key=lambda x: val(x))