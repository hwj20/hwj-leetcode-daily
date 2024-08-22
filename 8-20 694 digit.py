'''
476
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
'''

'''
water
'''

class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        now = 1
        while num > 0:
            if num%2 == 0:
                res += now
            now *= 2
            num //= 2
        return res