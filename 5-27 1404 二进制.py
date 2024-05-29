'''
1404. Number of Steps to Reduce a Number in Binary Representation to One
Medium
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.
'''

'''
二进制题，写了个很逆天的代码，居然过了
'''


class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        r = len(s)-1
        now = 0
        while r > 0:
            # print(ans)
            if int(s[r]) == 0 and now == 0:
                r -= 1
                ans += 1
            elif int(s[r]) == 1 and now == 1:
                r -= 1
                ans += 1
            elif int(s[r]) == 0 and now == 1:
                now = 1
                r -= 1
                ans += 2
            else:
                # int(s[r]) == 1 and now == 0:
                now = 1
                r -= 1
                ans += 2
        if now == 1:
            ans += 1
        return ans