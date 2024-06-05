'''
1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
'''

'''
遍历一遍
'''

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        count = Counter(words[0])
        for i in range(1,len(words)):
            word = words[i]
            con = Counter(word)
            for k,v in con.items():
                if k in count.keys():
                    if v<count[k]:
                        count[k] = v
            for k in count.keys():
                if k not in con.keys():
                    del(count[k])
        res = []
        for k,v in count.items():
            for i in range(v):
                res.append(k)
        return res
        '''
        Easier way
        min_freq = Counter(words[0])
        for word in words:
            min_freq &= Counter(word)
        return list(min_freq.elements())
        '''