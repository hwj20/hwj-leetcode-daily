'''
1137. N-th Tribonacci Number
Easy
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''

'''
简单递推，发现t了，用一个dict保存下答案
'''

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(lambda:-1)
        def findans(n):
            if d[n]  != -1:
                return d[n]
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            d[n] = findans(n-3)+findans(n-2)+findans(n-1)
            return d[n]
        return findans(n)