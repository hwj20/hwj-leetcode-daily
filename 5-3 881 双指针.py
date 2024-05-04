'''
881. Boats to Save People
Medium
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''

'''
第一反应双指针？你们怎么知道我打败了100%的python user
'''

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l,r = 0, len(people)-1
        ans = 0
        while l<r:
            if people[l]+people[r] <= limit:
                l += 1
                r -= 1
                ans += 1
            else:
                r -= 1
                ans += 1
        if l == r:
            ans += 1
        return ans