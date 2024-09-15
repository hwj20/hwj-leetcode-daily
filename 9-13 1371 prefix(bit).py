'''
1371
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
'''

'''
dp[i][a][k] = dp[i-1][a][k]+1 (not vowel) else ~k 
'''

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # vowel = {k:i for k,i in enumerate['a','e','i','o','u']}
        # print(vowel)
        # dp = [[0]*2 for _ in range(5) for _ in range(len(s))]
        # mx = 0
        # if s[0] in vowel
        #         dp[0][vowel[s[i]]][1] =  1
        #     else:
        #         for k in range(5):
        #             dp[0][k][0] =  1     
        #         mx = 1     
        # for i in range(1,len(s)):
        #     if s[i] in vowel:
        #         for k in range(5):
        #             for j in range(2):
                        
        #                 dp[i][k][j] =  dp[i-1][k][j]+1
        #             mx = max(mx,dp[i][k][j])
        #     else:
        #         for k in range(5):
        #             for j in range(2)
        #             dp[i][k][j] =  dp[i-1][k][j]+1
        #             mx = max(mx,dp[i][k][j])
        mapy = [-2] * 32
        mapy[0] = -1

        max_len = 0
        mask = 0

        for i, char in enumerate(s):
            print(mask)
            if char == 'a':
                mask ^= 1
            elif char == 'e':
                mask ^= 2
            elif char == 'i':
                mask ^= 4
            elif char == 'o':
                mask ^= 8
            elif char == 'u':
                mask ^= 16

            prev = mapy[mask]
            if prev == -2:
                mapy[mask] = i
            else:
                max_len = max(max_len, i - prev)

        return max_len                         