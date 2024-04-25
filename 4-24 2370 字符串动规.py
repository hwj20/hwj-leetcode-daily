'''
2370. Longest Ideal Subsequence
Medium

You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.
'''


'''
看起来像动态规划，实际上是用O(n)的方法把整个数组遍历一遍就行了，然后我t掉了...最后去问GPT，它又给我写回动态规划了
'''


class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # dp数组，记录以每个字符结尾的最长理想子序列的长度
        dp = [0] * 128  # 对于ASCII字符a-z，足够使用

        # 遍历给定字符串s中的每个字符
        for char in s:
            # 当前字符的ASCII值
            current = ord(char)

            # 检索当前字符可接受的ASCII值范围内的最大dp值
            max_len = 0
            # 仅在char的ASCII范围加减k内查找，因此时间复杂度为O(n*k)
            for j in range(max(0, current - k), min(127, current + k) + 1):
                max_len = max(max_len, dp[j])
            
            # 更新当前字符对应的dp值
            dp[current] = max_len + 1

        # 最后，返回dp数组中的最大值，即为最长理想子序列的长度
        return max(dp)