'''
664
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.
'''

'''
盲猜是个dp题,n=100可以试试保存步骤的dfs，这样的时间复杂度是(n^2)，因为每次都会更新最后的值，不会重复搜索，写错了，因为我们得处理每个点选不选，可以先选，然后不选，在选回来；eg. bacbcab；得改一下通项公式
'''

class Solution:
    
    def strangePrinter(self, s: str) -> int:
        n_s = ""
        for c in s:
            if n_s == "" or c != n_s[-1]:
                n_s += c
        s = n_s
        print(s)
        n = len(s)
        alive = [False]*n
        ans = [[0]*n for _ in range(n)]
        def dfs(l,r):
            # print(l,r)
            if l == r:
                ans[l][r] = 1
                return 1
            if l > r:
                # print("overflow")
                return 0
            if ans[l][r] != 0:
                return ans[l][r]
            # if alive[l]:
            #     return ans[l+1][r]
            tot = 1
            li = []
            a = dfs(l+1,r) + 1
            for i in range(l+1,r+1):
                # c = s[i]
                if s[i] == s[l]:
                    li.append(i)
            for i in range(len(li)):
                # tot += dfs(lidx,li[i]-1)
                # lidx = li[i]+1
                a = min(a,dfs(l,li[i]-1)+dfs(li[i]+1,r)) 
            ans[l][r] = a
            return a
        dfs(0,len(s)-1)
        # print(ans)
        return ans[0][-1]