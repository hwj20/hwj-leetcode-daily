'''
1122. Relative Sort Array
Easy
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
'''

'''
我感觉这道题挺难写的啊，为啥是easy
'''


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        mp = {}
        # narr = sorted(enumerate(arr2),key=lambda x:x[1])
        for i in range(len(arr2)):
            mp[arr2[i]] = i
        for i in range(1001):
            if i not in mp:
                mp[i] = 1001+i
        return sorted(arr1,key=lambda x: mp[x])
        