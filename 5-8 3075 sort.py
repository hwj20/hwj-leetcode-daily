'''
3075. Maximize Happiness of Selected Children
Medium
You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.
'''

'''
贪心题，每次拿最大的就行了，用sort就行了
'''



class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        happiness.sort(key=lambda x:-x)
        # print(happiness)
        for i in range(k):
            item = happiness[i]-(i)
            if item <= 0:
                break
            ans += item
        return ans