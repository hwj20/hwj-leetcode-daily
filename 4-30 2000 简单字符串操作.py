'''
2000. Reverse Prefix of Word
Easy
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.
'''

'''
简单的字符串，不解释了
'''

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        s = ''
        rev = True
        for c in word:
            if rev:
                s = c+s
            else:
                s = s+c
            if c == ch:
                rev = False
        return s