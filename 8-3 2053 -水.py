'''
2053
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
'''

'''
w
'''
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans =  []
        for a in arr:
            c = 0
            for b in arr:
                if a == b:
                    c += 1
                    if c == 2:
                        break
            if c == 1:
                ans.append(a)
        # print(ans)
        if k - 1 >= len(ans):
            return ""
        else:
            return  ans[k-1]       