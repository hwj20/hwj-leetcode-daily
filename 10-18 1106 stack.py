'''
1106
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

'''

'''
stack
'''

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        import copy
        s = []
        val_s = []
        temp = []
        for c in expression:
            if c == '&' or c == '!' or c == '|':
                s.append(c)
                continue
            if c == '(':
                # val_s.append(copy.deepcopy(temp))
                val_s.append(temp)
                temp = []
            if c == ')':
                op = s.pop()
                val = val_s.pop()
                if op == '&':
                    res = True
                    for v in temp:
                        res &= v
                if op == '|':
                    res = False
                    for v in temp:
                        res |= v
                if op == '!':
                    res = False if temp[0] else True
                temp = val
                temp.append(res)
                continue
            if c == 't':
                temp.append(True)
            if c == 'f':
                temp.append(False)
        return temp[0]