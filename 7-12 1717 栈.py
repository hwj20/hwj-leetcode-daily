'''
1717 Maximum Score From Removing Substrings
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
'''

'''
根据提示，有一个有限选的组合，然后判断剩下的组合就是了
'''

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s1 = []
        ans = 0
        opt,sec = 'ab','ba'
        if y > x:
            opt,sec = 'ba','ab'
            x,y = y,x
        for c in s:
            if c != 'a' and c != 'b':
                s2 = []
                for c1 in s1:
                    if s2 and s2[-1] == sec[0] and c1 == sec[1]:
                            s2.pop()
                            ans += y
                    else:
                        s2.append(c1)
                s1.clear()
            else:
                if s1 and s1[-1] == opt[0] and c == opt[1]:
                        s1.pop()
                        ans += x
                else:
                    s1.append(c)
        s2 = []
        for c1 in s1:
            if s2 and s2[-1] == sec[0] and c1 == sec[1]:
                    s2.pop()
                    ans += y
            else:
                s2.append(c1)
        return ans

