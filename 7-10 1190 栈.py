'''
1190
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.
'''

'''
一眼栈，但我cpu都要干烧了，抄了个答案，估计这辈子是想不出来了
'''
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                rev = ""
                while stack and stack[-1] != '(':
                    rev += stack.pop()
                if stack:
                    stack.pop()  # pop the opening bracket
                for c in rev:
                    stack.append(c)
            else:
                stack.append(char)

        return ''.join(stack)