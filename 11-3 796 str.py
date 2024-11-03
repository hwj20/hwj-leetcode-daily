'''
796
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
'''



class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            c = s[i]
            if c == goal[0]:
                # print(s[i:]+s[:i+1])
                if s[i:]+s[:i] == goal:
                    return True
        return False