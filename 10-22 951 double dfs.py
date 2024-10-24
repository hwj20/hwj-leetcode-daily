'''
951
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
'''

'''
have same items in the level x
double root
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # items1 = []
        # items2 = []
        # def dfs(now,dep,items):
        #     if now == None:
        #         return
        #     if len(items) <= dep:
        #         items.append([])
        #     items[dep].append(now.val)
        #     dfs(now.left,dep+1,items)
        #     dfs(now.right,dep + 1,items)
        # dfs(root1,0,items1)
        # dfs(root2,0,items2)
        # if len(items1) != len(items2):
        #     return False
        # for i in range(len(items1)):
        #     # flag = False
        #     t1 = sorted(items1[i])
        #     t2 = sorted(items2[i])
        #     if len(t1) != len(t2):
        #         return False
        #     for j in range(len(t1)):
        #         if t1[j] != t2[j]:
        #             return False
        # return True
        def dfs(now1,now2):
            if now1 == None and now2 == None:
                return True
            if now1 == None or now2 == None:
                return False
            if now1.val != now2.val:
                return False
            if now1.left == None and now2.left == None and now1.right == None and now2.right == None:
                return True
            if now1.left != None:
                if now2.left != None and now1.left.val == now2.left.val:
                    if dfs(now1.left,now2.left) and dfs(now1.right,now2.right):
                        return True
                if now2.right != None and now1.left.val == now2.right.val:
                    if  dfs(now1.left,now2.right) and dfs(now1.right,now2.left):
                        return True 
                return False
            if now1.right != None:
                if now2.left != None and now1.right.val == now2.left.val:
                    if dfs(now1.right,now2.left) and dfs(now1.left,now2.right):
                        return True
                if now2.right != None and now1.right.val == now2.right.val:
                    if  dfs(now1.right,now2.right) and dfs(now1.left,now2.left):
                        return True 
                return False                
            # print(now1.val,now2.val)
            return False
        return dfs(root1,root2)