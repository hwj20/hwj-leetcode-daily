'''
2058
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
'''

'''
找波峰波谷的位置?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        global prev,h,min_ans,max_ans
        prev,h = -1,-1
        min_ans,max_ans = -1,-1
        def dfs(now,pre,idx):
            global prev,h,min_ans,max_ans
            if now.next == None:
                return
            if (pre != -1) and ((pre > now.val and now.val < now.next.val) or (pre < now.val and now.val > now.next.val)):
                if prev != -1:
                    # print(idx-prev,min_ans)
                    if min_ans == -1:
                        min_ans = idx-prev
                    else:
                        min_ans = min(min_ans, idx-prev)
                prev = idx
                if h != -1:
                    max_ans = idx-h
                else:
                    h = idx
            dfs(now.next,now.val,idx+1)
        dfs(head,-1,0)
        return [min_ans,max_ans]
