'''
884
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
'''


'''

'''

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        
        a1,a2 = Counter(s1.split(' ')),Counter(s2.split(' '))
        res = []
        for a in a1:
            if a1[a] == 1 and a not in a2:
                res.append(a)
        for a in a2:
            if a2[a] == 1 and a not in a1:
                res.append(a)
        return res