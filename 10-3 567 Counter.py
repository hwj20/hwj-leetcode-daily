'''
567
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''

'''
sliding window
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter,defaultdict
        c = Counter(s1)
        l,r = -1,0
        cur = defaultdict(int)
        while r < len(s2):
            k = s2[r]
            if k not in c:
                # print('not in')
                l = r
                r += 1
                cur = defaultdict(int)                
                continue

            if cur[k] < c[k]:
                if r-l >= len(s1):
                    # print(r,l)
                    return True
                cur[k] += 1
                r += 1
            else:
                l += 1
                cur[s2[l]] -= 1
                while s2[l] != k:
                    l += 1
                    cur[s2[l]] -= 1
                cur[k] += 1
                r += 1

        return False
