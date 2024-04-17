# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
988. Smallest String Starting From Leaf
Medium

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
 
'''


'''
一眼递归保存答案，结果还是有坑，只能从叶子搜索答案，而不是向上贪心保存最小字符串
'''

ans = ['{']

def vis(now,cur):
    if now == None:
        return
    now.val = chr(now.val+97)
    cur = now.val+cur
    if now.left == None and now.right == None:
        ans[0] = min(ans[0],cur)
        return
    vis(now.left,cur)
    vis(now.right,cur)


class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        ans[0] = '{'
        vis(root,'')
        return ans[0]