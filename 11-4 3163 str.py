'''
3163
Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.
'''


class Solution:
    def compressedString(self, word: str) -> str:
        res = ''
        i = 0
        nxt = ''
        while i < len(word):
            j =  1
            c = word[i]
            while i+1 < len(word) and word[i+1] == word[i] and j != 9:
                i += 1
                j += 1
            res += str(j)+c
            i += 1
        return res
            