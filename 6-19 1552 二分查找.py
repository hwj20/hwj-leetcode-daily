'''
1552
Medium
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.
'''

'''
和昨天一样，二分查找
'''


class Solution(object):

    
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def check(position, k,m):
                last =  position[0]
                now = 1
                for i in range(1,len(position)):
                    if position[i]-last >= k:
                        last = position[i]
                        now += 1
                        if now == m:
                            return True
                return now >= m


        position.sort()
        l,r= 0,position[-1]
        while l<r:
            # print(l,r)
            mid = (l+r+1)//2
            if check(position, mid,m):
                l = mid
            else:
                r = mid-1
        return l