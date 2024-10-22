'''
2583
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root. 
'''

'''
dfs
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(level,now):
            if now == None:
                return
            if level > len(res):
                res.append(0)
            res[level-1]+= now.val
            dfs(level+1,now.left)
            dfs(level+1,now.right)
        dfs(1,root)
        if k > len(res):
            return -1
        res.sort()
        return res[-k]