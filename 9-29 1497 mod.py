'''
1497
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.
'''



class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = [0]*k
        for a in arr:
            if a % k == 0:
                continue
            # print(c)
            if c[k-(a%k)] == 0:
                c[a%k] += 1
            else:
                c[k-(a%k)] -= 1
        # print(c)
        return sum(c) == 0