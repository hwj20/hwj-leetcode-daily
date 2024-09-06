'''
3217
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
'''

'''
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # h = [None]
        nums = set(nums)
        def remove(fa,now):
            if now.val in nums:
                if fa != None:
                    fa.next = now.next
                    now = fa
                else:
                    pass
            # elif h[0] == None:
            #     h[0] = now
            if now.next != None:
                remove(now,now.next)
        while head != None and head.val in nums:
            head = head.next
        if head == None:
            return None
        remove(None,head)
        return head  