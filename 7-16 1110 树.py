'''
1110
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

'''


'''
dfs 秒了，我也不知道为什么能过，反正过了就是了
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)
        def dfs(now):
            if now == None:
                return None
            lres = dfs(now.left)
            rres =  dfs(now.right)
            now.left = lres
            now.right = rres
            if now.val in to_delete:
                ans.append(lres)
                ans.append(rres)
                return None
            else:
                return now
        ans.append(dfs(root))
        return [k for k in ans if k != None]
