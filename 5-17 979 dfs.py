'''
979. Distribute Coins in Binary Tree
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.
'''


'''
有借必有贷 借贷必相等（狗头。打败了100%的python用户，我果然是古希腊掌管dfs的神
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        def dfs(now):
            if now == None:
                return 0
            l = dfs(now.left)
            r = dfs(now.right)
            ans[0] += abs(now.val-1-l-r)
            return -(now.val-1-l-r) # 欠的钱
        dfs(root)
        return ans[0]