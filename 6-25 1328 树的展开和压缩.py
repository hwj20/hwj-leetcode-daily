'''
1382

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
'''

'''
平衡二叉树
now.right,now.right.left = now.right.left,now;
旋得我腦闊青痛，而且我的輸入法怎麼變繁體了，果然我是50w是吧
沒事，GPT也沒旋對，起碼我們智力水平差不多嘿嘿嘿
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Convert BST to sorted array
        def inorderTraversal(node):
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right) if node else []
        
        sorted_array = inorderTraversal(root)
        
        # Convert sorted array to balanced BST
        def sortedArrayToBST(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])
            return root
        
        return sortedArrayToBST(sorted_array)
        # global r
        # r = root
        # def dfs(fa,now,is_left):
        #     global r
        #     if now == None:
        #         return 0
        #     dl,dr = dfs(now,now.left,True),dfs(now,now.right,False)
        #     # print(dl,dr)
        #     if dr-dl > 1:
        #         if now == r:
        #             r = now.right
        #         if fa != None:
        #             if is_left:
        #                 fa.left = now.right
        #             else:
        #                 fa.right = now.right
        #         tmp = now.right.left
        #         now.right.left = now
        #         now.right = tmp
        #         # now.right,now.right.left = now.right.left,now
        #         return dl+2
        #     if dl-dr > 1:
        #         if now == r:
        #             r = now.left
        #         if fa != None:
        #             if is_left:
        #                 fa.left = now.left
        #             else:
        #                 fa.right = now.left
        #         tmp = now.left.right
        #         now.left.right = now
        #         now.left = tmp
        #         # now.left,now.left.right = now.left.right,now
        #         return dr+2
        #     return max(dl,dr)+1
        # dfs(None,root,False)
        # return r            