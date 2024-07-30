'''
1653
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
'''


'''
min(lb-a in the right, ra - b in the left)
'''

class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)
        pb,aa = [0]*n,[0]*n
        pb[0] = 1 if s[0] == 'b' else 0
        aa[n-1] = 1 if s[n-1] == 'a' else 0
        for i in range(1,n):
            if s[i] == 'b':
                pb[i] = pb[i-1]+1
            else:
                pb[i] = pb[i-1]
        for i in range(n-2,-1,-1):
            if s[i] == 'a':
                aa[i] = aa[i+1]+1
            else:
                aa[i] = aa[i+1]
        ans = aa[0]
        # print(pb,aa)
        for i in range(n):
            f = -1 if s[i] == 'a' else 0
            ans = min(pb[i]+aa[i]+f,ans)
        return ans