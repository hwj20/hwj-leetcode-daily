'''
140. Word Break II
Hard
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

'''
枚举的时间复杂度是 2^10*1000（假设每个单词长度为2），感觉能卡过，如果要提升时间的话，可以按照首字母做一个dict表
我这个dfs居然打过了90%的人，太逆天了
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        import copy

        res = []
        temp = []
        # used = [False]*len(wordDict)
        def dfs(now):
            # print(now,temp)
            if now == len(s):
                res.append(' '.join(temp))
                # print(res)
                return
            for i in range(len(wordDict)):
                if len(wordDict[i])+now > len(s):
                    continue
                if wordDict[i] == s[now:now+len(wordDict[i])]:
                    temp.append(wordDict[i])
                    # used[i] = True
                    dfs(now+len(wordDict[i]))
                    # used[i] = False
                    temp.pop()
        dfs(0)
        return res
                
