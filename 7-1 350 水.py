'''
350

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        count1,count2 = Counter(nums1),Counter(nums2)
        ans = []
        for k,v in count1.items():
            if k in count2:
                for i in range(min(count1[k],count2[k])):
                    ans.append(k)
        return ans