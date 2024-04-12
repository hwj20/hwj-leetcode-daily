"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining
"""


"""
两个循环搞定
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0,0
        ans = 0
        while(r < len(height)):
            if height[r] >= height[l]:
                m = height[l]
                while(l < r):
                    ans += m-height[l]
                    l += 1
            r += 1

        l,r = len(height)-1,len(height)-1
        while (l >= 0):
            if height[l] > height[r]:
                m = height[r]
                while (l<r):
                    ans += m - height[r]
                    r -= 1
            l -= 1
        return ans