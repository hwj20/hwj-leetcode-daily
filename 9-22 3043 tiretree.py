'''
3043
You are given two arrays with positive integers arr1 and arr2.

A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.

A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.

You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.

Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.


'''
'''
tire tree
'''

class TreeNode():
    def __init__(self,val=None,children=None):
        self.val = val
        if not children:
            self.children = []
        else:
            self.children = children

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
            return 0
        else:
            for c in now.children:
                print(c.val)
                if s[0] == c.val:
                    return self.findprefix(s[1:],c)+1
            return 0

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = TireTree()
        for arr in arr2:
            t.add(str(arr))
        ans = 0
        for arr in arr1:
            if len(str(arr)) <= ans:
                continue
            ans = max(ans,t.findprefix(str(arr),t.root))
        return ans
        