# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt,values = 0,[]
        now = head
        while now != None:
            # print(now.val)
            cnt += 1
            # values.append(now.val)
            now = now.next
        if cnt == 0:
            return [None for i in range(k)]

        max_len = cnt//k
        to_filled = cnt % k
        now, cur_len = head,0
        ans = [now]
        print(max_len,to_filled)

        while now != None:
            print(now.val)
            cur_len += 1
            if to_filled > 0 and cur_len == max_len+1:
                to_filled -= 1
                now_next = now.next
                now.next = None
                now = now_next
                if now_next != None:
                    ans.append(now_next)
                cur_len = 0
            elif to_filled == 0 and cur_len == max_len:
                now_next = now.next
                now.next = None
                now = now_next
                if now_next != None:
                    ans.append(now_next)
                cur_len = 0
            else:
                now = now.next
        if len(ans) < k:
            print('----')
            print(len(ans),k)
            for i in range(k-len(ans)):
                ans.append(None)
        return ans

        