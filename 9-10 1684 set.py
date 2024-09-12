'''
1684
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
'''

'''

'''
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        d = set([x for x in allowed])
        for w in words:
            flag = False
            for c in w:
                if c not in d:
                    flag = True
                    break
            if not flag:
                res += 1
        return res
