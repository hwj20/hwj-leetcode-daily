'''
1331
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
'''




class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        import copy
        n_arr = copy.deepcopy(arr)
        n_arr.sort()
        r = 1
        m = {n_arr[0]:1}
        for i in range(1,len(arr)):
            if n_arr[i] != n_arr[i-1]:
                r += 1
            m[n_arr[i]] = r 

        # print(arr)
        return [m[a] for a in arr]