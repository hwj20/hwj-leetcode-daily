'''
3016
You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.
'''

'''
类似于哈夫曼树
'''

class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        import string
        count = Counter(word)
        li = list(string.ascii_lowercase)
        li.sort(key=lambda x:-count[x])
        now = 1
        tot = 0
        ans = 0
        for c in li:
            if count[c] == 0:
                break
            ans += count[c]*now
            tot += 1
            if tot == 8:
                tot = 0
                now += 1
        return ans
