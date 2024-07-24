'''
1636
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
'''

'''
排序
'''
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def val(x):
            global cnt
            return (cnt[x],-x)
        global cnt
        from collections import Counter
        cnt = Counter(nums)
        return sorted(nums,key=lambda x:val(x))