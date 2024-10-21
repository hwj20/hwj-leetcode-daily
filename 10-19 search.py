
'''
1593. Split a String Into the Max Number of Unique Substrings
Medium
Topics
Companies
Hint
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

'''

'''
deep search
'''

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        now = []
        ans = [0]
        def dfs(t):
            if t == "":
                ans[0] = max(ans[0],len(now))
                # print(now)
                return
            temp = ""
            for i in range(len(t)):
                temp += t[i]
                if temp in now:
                    continue
                now.append(temp)
                dfs(t[i+1:])
                now.pop()
        dfs(s)
        return ans[0]
