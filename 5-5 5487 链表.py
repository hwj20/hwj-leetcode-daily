'''
2487. Remove Nodes From Linked List
Medium
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list
'''


'''
递归，return最大值的点，可以，我两分钟写完了，然后打败了6%的python user哈哈哈，他们用的stack，比我这个递归快
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def vis(now):
            if now.next == None:
                return now
            res = vis(now.next)
            if now.val < res.val:
                return res
            now.next = res
            return now
        return vis(head)