'''
2601
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

'''

import bisect

def get_primes(n):
    res = [2]
    for i in range(3,n+1):
        f = True
        for j in range(2,int(sqrt(i))+1):
            if i % j == 0:
                # print(i,j)
                f = False
                break
        if f:
            res.append(i)
    return res

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        f = True
        p = get_primes(2000)
        # print(p)
        for i in range(len(nums)):
            l = 0
            if i > 0:
                l = nums[i-1]
            if nums[i] <= l:
                return False
            idx = bisect.bisect_left(p, nums[i]-l)
            # print(idx)
    
            # 如果 idx == 0，说明列表中没有比 target 小的值
            if idx == 0:
                continue
            else:
                nums[i] -= p[idx-1]
        print(nums)
        return True