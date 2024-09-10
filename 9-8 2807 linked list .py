'''
2807. Insert Greatest Common Divisors in Linked List
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''

'''
vis node
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(now,flag):
            if now == None:
                return
            if now.next != None and flag:
                node = ListNode(val=gcd(now.val,now.next.val),next=now.next)
                now.next = node
            flag = not flag
            dfs(now.next,flag)
        dfs(head, True)
        return head
        