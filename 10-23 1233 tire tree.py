'''
1233
Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
'''

'''
tire tree
'''

class Node:
    def __init__(self,val):
        self.v = val
        self.children = []
        self.end = False

class Tree:
    def __init__(self,root):
        self.r = root
    def add(self,li):
        return self._add(li,self.r)
    def _add(self,li,now:Node):
        if li == []:
            # print('end')
            now.end = True
            return True
        ch = li[0]
        for node in now.children:
            # print(node.v,ch)
            if node.v == ch:
                # print(node.v, ch)
                if node.end:
                    return False
                return self._add(li[1:],node)
        node = Node(ch)
        now.children.append(node)
        self._add(li[1:],node)
        return True
    def print_tree(self):
        ans = []
        self._print(self.r,ans,'')
        return ans
    def _print(self,now:Node,ans,now_ch):
        if now.end:
            ans.append(now_ch)
            return
        for c in now.children:
            n_str = now_ch +'/'+ c.v
            self._print(c,ans,n_str)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Node('')
        tree = Tree(root=root)
        ans = []
        for f in folder:
            # for c in f.split('/'):
            #     if c != '':
            li = f.split('/')
            # print(li)
            tree.add(li[1:])
                # ans.append(f)
        
        return tree.print_tree()

