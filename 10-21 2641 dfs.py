'''
2641
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def dfs1(now,depth,parent):
            if now == None:
                return 0
            if len(res) <= depth:
                res.append(0)
            res[depth] += now.val
            v1 = dfs1(now.left,depth+1,now)
            v2 = dfs1(now.right,depth+1,now)
            now.s = v1+v2
            now.p = parent
            now.d = depth
            return now.val
        dfs1(root,0,None)
        def dfs2(now):
            if now == None:
                return
            if now.p != None:
                now.val = res[now.d]-now.p.s
            else:
                now.val = 0
            dfs2(now.left)
            dfs2(now.right)
        dfs2(root)
        return root
