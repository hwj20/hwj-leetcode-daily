'''
1915. Number of Wonderful Substrings
Medium

A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.
'''

'''
做不来，心情不好，看答案吧；woc，位运算枚举
'''


class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        toBit = {c: 1 << i for i, c in enumerate(ascii_lowercase[:10])}
        mask = 0

        count = defaultdict(int)
        count[0] = 1

        for c in word:
            mask ^= toBit[c]
            count[mask] += 1

        res = 0
        for mask, cnt in count.items():
            res += cnt * (cnt - 1) // 2
            for i in range(10):
                mask2 = mask ^ (1 << i)
                if mask2 < mask:
                    res += cnt * count.get(mask2, 0)

        return res