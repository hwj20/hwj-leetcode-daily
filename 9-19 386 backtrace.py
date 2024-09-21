'''
386
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
'''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        # i = ''
        def find(now,n):
            for i in range(10):
                cur = now*10+i
                if cur == 0:
                    continue
                if cur <= n:
                    res.append(cur)
                    find(cur,n)
                else:
                    break
        find(0,n)
        return res
