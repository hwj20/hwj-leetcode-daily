'''
2696
You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.
'''


class Solution:
    def minLength(self, s: str) -> int:
        cnt = 0
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) > 1:
                if stack[-2] == 'A' and stack[-1] == 'B':
                    cnt += 2
                    stack.pop()
                    stack.pop()
                    continue
                if stack[-2] == 'C' and stack[-1] == 'D':
                    cnt += 2
                    stack.pop()
                    stack.pop()
        return len(s)-cnt
                

