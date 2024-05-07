'''
2816. Double a Number Represented as a Linked List
Medium

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.
'''
'''
和昨天的题一样，直接递归就行了
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def vis(now):
            if now.next == None:
                now.val = now.val*2
                res = now.val // 10
                now.val = now.val % 10
                return res
            r = vis(now.next)
            now.val = now.val*2 + r
            res = now.val // 10
            now.val = now.val % 10      
            return res
        re = vis(head)
        if re != 0:
            h = ListNode(re,head)
            return h
        return head