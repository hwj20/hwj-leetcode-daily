'''
624
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.
'''

'''
找最大最小的
'''
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi,mx = [],[]
        for i in range(len(arrays)):
            a = arrays[i]
            mi.append((a[0],i))
            mx.append((a[-1],i))
        mi.sort()
        mx.sort()
        if mi[0][1] != mx[-1][1]:
            return mx[-1][0]-mi[0][0]
        else:
            return max(mx[-2][0]-mi[0][0],mx[-1][0]-mi[1][0])
        