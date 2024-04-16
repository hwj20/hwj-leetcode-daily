# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
623. Add One Row to Tree
Medium
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree
'''

'''
带depth 深度搜搞定，最近是捅树窝了吗...
'''
# tar_dep = -1
# tar_val = -1
ans = None

def vis(now,dep,dr='l',fa=None,tar_dep=-1,tar_val=-1):
    if tar_dep == dep:
        # print(now.val)
        n_node = TreeNode(val=tar_val,left=None, right=None)
        if dr == 'l':
            n_node.left = now
            fa.left=n_node
        else:
            n_node.right = now
            fa.right=n_node
        return
    if now == None:
        return
    vis(now.left,dep+1,'l',now,tar_dep,tar_val)
    vis(now.right,dep+1,'r',now,tar_dep,tar_val)

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        tar_dep = depth
        tar_val = val
        if depth == 1:
            return TreeNode(val=val,left=root,right=None)
        vis(root,1,'l',None,depth,val)
        return root