'''
440
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
'''


class Solution:
        # global cnt
        # cnt = -1
        # def find(now,k):
        #     global cnt
        #     cnt += 1
        #     # print(cnt,now)
        #     if cnt == k:
        #         return now
        #     for i in range(10):
        #         cur = now*10+i
        #         if cur == 0:
        #             continue
        #         if cur <= n:
        #             # cnt += 1
        #             res = find(cur,k)
        #             if res:
        #                 return res
        #         else:
        #             break
        #     return None
        # return find(0,k)
        def getReqNum(self, a, b, n):
            gap = 0
            while a <= n:
                gap += min(n + 1, b) - a
                a *= 10
                b *= 10
            return gap

        def findKthNumber(self, n: int, k: int) -> int:
            num = 1
            i = 1
            while i < k:
                req = self.getReqNum(num, num + 1, n)
                if i + req <= k:
                    i += req
                    num += 1
                else:
                    i += 1
                    num *= 10
            return num
            