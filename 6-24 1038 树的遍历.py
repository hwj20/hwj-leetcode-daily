'''
1038
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''


'''
递归遍历
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(now,r_sum):
            res = now.val
            if now.right != None:
                res += dfs(now.right,r_sum)
                now.val = res
            now.val += r_sum
            if now.left != None:
                res += dfs(now.left,now.val)
            # print(now,res)

            return res
            
        dfs(root,0)
        return root