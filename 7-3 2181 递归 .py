'''
2181
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
'''

'''
递归
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def dfs(now):
            if now.next == None:
                return 0,None
            if now.val == 0:
                now.val,now.next = dfs(now.next)
                # if r_node 
                return 0,now
            else:
                res,r_node = dfs(now.next)
                # if r_node = 
                res += now.val
                return res,r_node
        _,r = dfs(head)
        return r
