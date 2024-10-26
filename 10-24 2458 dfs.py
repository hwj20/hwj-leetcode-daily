'''
2458. Height of Binary Tree After Subtree Removal Queries
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
 
'''

'''
hash - node
udpate self.val_c = [height.l, height.r] in self.parent and self.isleft
wrong idea
just pre compute
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def update(now, isleft,val):

#     if isleft:
#         mx = max(val,now.hr)+1
#         if mx < now.h:
#             if now.parent == None:
#                 return mx
#             else:
#                 return update(now.parent, now.isleft,mx)
#     else:
#         mx = max(now.hl,val)+1
#         if mx < now.h:
#             if now.parent == None:
#                 return mx
#             else:
#                 return update(now.parent, now.isleft,mx)
#     return -1
def print_tree(node, level=0, label="."):
    if node is not None:
        # 先打印右子树
        print_tree(node.right, level + 1, "R")
        
        # 打印当前节点值，缩进表示层级
        print(" " * (4 * level) + f"{label}: {node.val}")
        
        # 打印左子树
        print_tree(node.left, level + 1, "L")
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        m = {}
        
        def dfs(now):
            if now == None:
                return 0
            now.hl = dfs(now.left)
            now.hr = dfs(now.right)
            now.h = max(now.hl,now.hr)+1
            m[now.val] = 0
            return now.h
        def dfs2(now,other):
            if now == None:
                return
            # print(now.val,other)
            other -= 1
            if now.hr > now.hl:
                other = max(other,now.hl)
                if other < now.hr:
                    m[now.right.val] =  now.hr - other
                    dfs2(now.right,other) 
            if now.hl > now.hr:
                other = max(other,now.hr)
                if other < now.hl:
                    m[now.left.val] =  now.hl - other
                    dfs2(now.left,other) 
        dfs(root)
        dfs2(root,0)
        # print_tree(root)
        ans = []
        m[root.val] = root.h-1
        # print(m)
        for q in queries:
            ans.append(root.h-1-m[q])
        return ans