'''
633. Sum of Square Numbers
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
'''

'''
a^2+b^2= (a+b)^2-2ab = c a,b<sqrt(c)
'''

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        finds = set()
        t = int(sqrt(c))
        finds.add(0)
        for i in range(t+1):
            now = i*i
            finds.add(now)
            if (c-now) in finds:
                return True
        return False
        