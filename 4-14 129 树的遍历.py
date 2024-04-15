# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
129. Sum Root to Leaf Numbers
Medium
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
'''

'''
看起来像树的遍历题;实际上就是，真不懂为什么有medium难度
'''


ans = [0]

def vis(now, cur):
    if now == None:
        return

    num = cur*10+now.val
    if now.left == None and now.right == None:
        ans[0] += num
        return
    vis(now.left,num)
    vis(now.right,num)

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans[0] = 0
        vis(root,0)
        return ans[0]