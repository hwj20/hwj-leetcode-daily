'''
650
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
'''

'''
dfs
'''
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        global ans
        ans = n+1
        def dfs(now,cp,steps):
            global ans
            if now == n:
                ans = min(ans,steps)
                return
            if steps >= ans or now > n:
                return
            # if cp == 0:
            #     dfs(now,now,steps+1)
            # else:
                # dfs(now+cp,cp,steps+1)
                # dfs(now,0,steps+1)
            dfs(now+cp,cp,steps+1)
            dfs(now*2,now,steps+2)

        dfs(1,1,1)
        return ans