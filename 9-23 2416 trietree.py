'''
2416
You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.
'''
'''
trie tree
'''


class TreeNode():
    def __init__(self,val=None,children=None):
        self.val = val
        if not children:
            self.children = []
        else:
            self.children = children
        self.cnt = 0

class TireTree():
    def __init__(self):
        self.root = TreeNode()
    def add(self,s):
        # if not self.root:
        #     self.root = TreeNode(s[0],[])
        #     self._add(s[1:],self.root)
        # else:
        self. _add(s,self.root)
    def _add(self,s:str,now:TreeNode):
        now.cnt += 1
        if s == '':
            return
        else:
            for c in now.children:
                if s[0] == c.val:
                    self._add(s[1:],c)
                    return
            now.children.append(TreeNode(s[0],[]))
            self._add(s[1:],now.children[-1])
    def findprefix(self,s:str,now:TreeNode):
        if s == '':
            return now.cnt
        else:
            for c in now.children:
                # print(c.val)
                if s[0] == c.val:
                    return now.cnt + self.findprefix(s[1:],c)
            return 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = TireTree()
        for w in words:
            t.add(w)
        t.root.cnt = 0
        res = []
        for w in words:
            # tmp = 0
            # for i in range(1,len(w)+1):
            #     tmp += t.findprefix(w[:i],t.root)
            res.append(t.findprefix(w,t.root))
        return res

        