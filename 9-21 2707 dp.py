''
2707
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.
'''


'''
match string
violence
'''

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        prev_max = 0
        for i in range(n):
            # dp[i] = max(dp[i-1],dp[i])
            for word in dictionary:
                is_match = True
                for j in range(len(word)): 
                    if i+j >= len(s) or word[j] != s[i+j]:
                        is_match =False
                        break 
                if is_match:
                    dp[i+len(word)-1] = max(prev_max+ len(word), dp[i+len(word)-1])
            # dp[i][0] = prev_max
            prev_max = max(prev_max,dp[i])
        # print(dp,len(s))
        return n-prev_max


        