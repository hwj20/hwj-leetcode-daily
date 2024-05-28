'''
1208. Get Equal Substrings Within Budget
Medium
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ord values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
'''

'''
用二分查找过了，但是时间不如直接用window，生气气
'''

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        n = len(s)
        cost = [0]*n
        sm = [0]*(n+1)
        cost[0],sm[0] = abs(ord(s[0])-ord(t[0])),0
        for i in range(1,n):
            cost[i] = abs(ord(s[i])-ord(t[i]))
            sm[i] = sm[i-1]+cost[i-1]
        sm[n] = sm[n-1]+cost[n-1]
        mx = 0
        print(sm)
        for i in range(n+1):
            if n+1-i < mx:
                break
            index = bisect.bisect_right(sm, maxCost+sm[i])
            if index == n+1:
                mx = max(mx,n-i)
                continue
            # print(index)
            if sm[index] ==  maxCost+sm[i]:
                mx = max(mx,index-i)
            else:
                mx = max(mx,index-i-1)
            
            # for j in range(n+1,i+mx-1):
            #     if sm[j]-sm[i] <= maxCost:
            #         mx = j-i
            #         # print(j,i)
            #     elif:
            #         continue
        return mx
        