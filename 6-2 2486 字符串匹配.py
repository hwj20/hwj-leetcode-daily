'''
2486. Append Characters to String to Make Subsequence
Medium
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
'''

'''
字符串匹配题，实际上需要求出来t的最长前缀子字符串；直接匹配一次就是了
'''


class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ti = 0
        for c in s:
            if c == t[ti]:
                ti  += 1
                if ti == len(t):
                    break
        return len(t)-ti
        