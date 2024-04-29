'''
2997. Minimum Number of Operations to Make Array XOR Equal to K
Medium
You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:

Choose any element of the array and flip a bit in its binary representation. Flipping a bit means changing a 0 to 1 or vice versa.
Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.

Note that you can flip leading zero bits in the binary representation of elements. For example, for the number (101)2 you can flip the fourth bit and obtain (1101)2.
'''

'''
看了一眼，感觉就是xor结果再和k比较一下有多少位不同...就是这样，过了，嘿嘿
'''


class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        xor_sum = 0
        for n in nums:
            xor_sum = xor_sum ^ n
        # print(xor_sum) 
        tmp = k ^ xor_sum
        ans = 0
        while tmp != 0:
            if tmp&1:
                ans += 1
            tmp >>= 1
        return ans