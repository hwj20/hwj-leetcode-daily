# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
404. Sum of Left Leaves
Easy
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
'''


'''
Easy 题，题号404,纪念一下
'''

ans = [0]

def dfs(now):
    if now == None:
        return False
    if now.left == None and now.right == None:
        return True
    if dfs(now.left):
        ans[0] += now.left.val
    dfs(now.right) 
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans[0] = 0
        dfs(root)
        return ans[0]