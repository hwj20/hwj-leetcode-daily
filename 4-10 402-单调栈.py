"""
402. Remove K Digits
Medium
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
"""


"""
想法：保持删除最多的前导0，能够达到最低的位数；再保留数组中最低的几位数
debug：错误的想法，折腾半天，答案是单调栈；嗯，我的解法里也有个栈......
"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for n in num:
            while( stack and int(stack[-1]) > int(n) and k):
                stack.pop()
                k -= 1
            stack.append(str(n))

        while(k):
            stack.pop()
            k -= 1
            
        i = 0
        while( i <len(stack) and stack[i] == "0" ):
            i += 1
            
        return ''.join(stack[i:]) if (len(stack[i:]) > 0) else "0"      