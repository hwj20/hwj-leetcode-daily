'''
1325. Delete Leaves With a Given Value
Medium
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
'''

'''
dfs 跑一趟吧，果然，我是古希腊掌握 dfs 的神
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def dfs(now):
            if now == None:
                return True
            l = dfs(now.left)
            r = dfs(now.right)
            if l:
                now.left = None
            if r:
                now.right = None
            if l and r and now.val==target:
                return True
        if  dfs(root):
            return None
        else:
            return root
        