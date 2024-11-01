'''
1957
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.
'''



class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        prev = ''
        ct = 0
        ns = ''
        while i < len(s):
            if s[i] == prev:
                ct += 1
                if ct < 2:
                    ns += s[i]
            else:
                ct = 0
                ns += s[i]
            prev = s[i]
            i += 1
        return ns
