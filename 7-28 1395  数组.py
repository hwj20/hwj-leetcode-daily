'''
1395
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
'''

'''
其实枚举能过大部分数据hhh
逆向思维，找到所有波峰波谷；也可以找比它大和比它小的
'''


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = n*(n-1)*(n-2)/6
        bf,af = [0]*(n+1),[0]*(n+1)

        for i in range(n):
            for j in range(i-1,-1,-1):
                if rating[i] > rating[j]:
                    bf[i] += 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if rating[i] > rating[j]:
                    af[i] += 1  

        for i in range(n):
            ans -= bf[i]*af[i]

        bf,af = [0]*(n+1),[0]*(n+1)
        for i in range(n):
            for j in range(i-1,-1,-1):
                if rating[i] < rating[j]:
                    bf[i] += 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if rating[i] < rating[j]:
                    af[i] += 1
        for i in range(n):
            ans -= bf[i]*af[i]
        return int(ans)
        # for a in l:
        #     if a < 3:
        #         continue
        #     ans += a*(a-1)*(a-2)/6
        # return ans
        # cnt = 0

        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,n):
        #             if (rating[i] > rating[j] > rating[k]) or (rating[i] < rating[j] < rating[k]):
        #                 cnt += 1
        # return cnt