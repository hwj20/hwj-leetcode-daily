'''
131. Palindrome Partitioning
Medium
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.
'''

'''
枚举方法可以变成一次枚举一段s，这样就不用挤在最后来判断了
'''


class Solution(object):
    def partition(self, s):
        import copy
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def is_palindrome(ns):
            return ns == ns[::-1]

            

        def dfs(now,ans):
            if now == len(s):
                for ns in ans:
                    if not is_palindrome(ns):
                        return
                res.append(copy.deepcopy(ans))
                return
            # if ans == []:
            #     ans = [s[now]]
            ans.append(s[now])
            dfs(now+1,ans)
            ans.pop()
            ns = ans[-1]+s[now]
            # if is_palindrome(ns):
            save = ans[-1]
            ans[-1] = ns
            dfs(now+1,ans)
            ans[-1] = save

        dfs(1,[s[0]])
        return res