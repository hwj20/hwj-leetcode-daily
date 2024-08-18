'''
264
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
'''

'''
暴力打个表(不行，250000只有381个)
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # res = [1]
        # factors = [2,3,5,6,10,15,30]
        # i = 1
        # while len(res)<5000:

        #     for j in range(i+1):
        #         for k in range(i+1-j):
        #             now = 1
        #             for l2 in range(j):
        #                 now *= 2
        #             for l3 in range(k):
        #                 now *= 3
        #             for l5 in range(i-j-k):
        #                 now *= 5
        #             res.append(now)
        #     i += 1
        # res.sort()
        # # print(res)
        # return res[n-1]   
        p2, p3, p5 = 1, 1, 1
        product2, product3, product5 = 1, 1, 1
        # Final merged linked list and pointer
        ugly = [0] * (n+1)
        p = 1

        # Start merging 3 linked list, until finding the nth ugly number
        while p <= n:
            min_val = min(product2, product3, product5)
            ugly[p] = min_val
            p += 1
            # move forward the corresponding linked list pointer
            if min_val == product2:
                product2 = ugly[p2] * 2
                p2 += 1
            if min_val == product3:
                product3 = ugly[p3] * 3
                p3 += 1
            if min_val == product5:
                product5 = ugly[p5] * 5
                p5 += 1
        
        return ugly[n]'''
264
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
'''

'''
暴力打个表(不行，250000只有381个)
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # res = [1]
        # factors = [2,3,5,6,10,15,30]
        # i = 1
        # while len(res)<5000:

        #     for j in range(i+1):
        #         for k in range(i+1-j):
        #             now = 1
        #             for l2 in range(j):
        #                 now *= 2
        #             for l3 in range(k):
        #                 now *= 3
        #             for l5 in range(i-j-k):
        #                 now *= 5
        #             res.append(now)
        #     i += 1
        # res.sort()
        # # print(res)
        # return res[n-1]   
        p2, p3, p5 = 1, 1, 1
        product2, product3, product5 = 1, 1, 1
        # Final merged linked list and pointer
        ugly = [0] * (n+1)
        p = 1

        # Start merging 3 linked list, until finding the nth ugly number
        while p <= n:
            min_val = min(product2, product3, product5)
            ugly[p] = min_val
            p += 1
            # move forward the corresponding linked list pointer
            if min_val == product2:
                product2 = ugly[p2] * 2
                p2 += 1
            if min_val == product3:
                product3 = ugly[p3] * 3
                p3 += 1
            if min_val == product5:
                product5 = ugly[p5] * 5
                p5 += 1
        
        return ugly[n]