'''
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
'''

'''
昨天有点事，没做，这个直接return s减去1个的字符就是了的长度就是了
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(s)
        ans = len(s)
        offset = 0
        for k,v in count.items():
            if v%2 == 1:
                offset = 1
                ans -= 1
        return ans+offset