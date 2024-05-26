'''
552
Hard

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.
'''


'''
组合数题，但是今天赶due，抄下答案
'''




class Solution(object):
    MOD = 1000000000 + 7
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        prevDP = [[1] * 3 for _ in range(2)]

        for i in range(1, n + 1):
            newDP = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    # Pick P
                    newDP[a][l] += prevDP[a][2]
                    newDP[a][l] %= self.MOD
                    if a > 0:
                        # Pick A
                        newDP[a][l] += prevDP[a - 1][2]
                        newDP[a][l] %= self.MOD
                    if l > 0:
                        # Pick L
                        newDP[a][l] += prevDP[a][l - 1]
                        newDP[a][l] %= self.MOD
            prevDP = newDP

        return prevDP[1][2]