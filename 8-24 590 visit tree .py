'''
145. Binary Tree Postorder Traversal
'''


'''
water
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(now):
            if now == None:
                return 
            for child in now.children:
                dfs(child)
            ans.append(now.val)
        dfs(root)
        return ans