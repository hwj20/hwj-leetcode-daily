'''
592
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
'''


'''
分母全乘，然后约分
'''

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num,dom = [],[]
        sign = True
        # is_one = False
        for c in expression:
            if c == '-':
                sign = False
                continue
            if c == '+':
                sign = True
                continue
            if c.isdigit():
                if int(c) == 0:
                    if len(num) > len(dom):
                        num[-1] *= 10
                        continue
                    else:
                        dom[-1] *= 10
                        continue
                if len(num) > len(dom):
                    dom.append(int(c))
                else:
                    if sign:
                        num.append(int(c))
                    else:
                        num.append(-int(c))
                continue
        # print(num,dom)
        mul = 1
        for d in dom:
            mul *= d
        s = 0
        for i in range(len(dom)):
            s += num[i]*mul/dom[i]
        if s == 0:
            return "0/1"
        else:
            for d in dom:
                if s % d == 0:
                    mul  /= d
                    s /= d
            for d in range(2,int(sqrt(max(abs(s),mul)))+1):
                if d> abs(s):
                    break
                while s % d == 0 and mul %d == 0:
                    mul  /= d
                    s /= d
            return str(int(s))+'/'+str(int(mul))
                