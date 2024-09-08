'''
1367. Linked List in Binary Tree
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
'''
'''
dfs， The first version will repeatly compare nodes.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        # def dfs(nh,now):
        #     if nh == None:
        #         return True
        #     if now == None:
        #         return False
        #     if nh.val == now.val:
        #         if dfs(nh.next,now.left):
        #             return True
        #         if dfs(nh.next,now.right):
        #             return True

        #     if dfs(head,now.left):
        #         return True
        #     if dfs(head,now.right):
        #         return True
        # return dfs(head,root)        # 深度优先搜索：匹配链表和树的子结构
        def dfs(nh, now):
            if nh is None:  # 如果链表遍历完了，说明找到子路径
                return True
            if now is None:  # 树到头了但链表还没完，说明不匹配
                return False
            if nh.val == now.val:  # 如果当前节点匹配，继续往左右子树递归
                if dfs(nh.next, now.left) or dfs(nh.next, now.right):
                    return True
            return False  # 不匹配返回 False
        
        # 遍历树的每个节点
        def traverse(now):
            if now is None:
                return False
            if dfs(head, now):  # 如果从当前节点能匹配链表
                return True
            return traverse(now.left) or traverse(now.right)  # 继续遍历左右子树
        
        return traverse(root)