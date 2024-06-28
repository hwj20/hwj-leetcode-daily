'''
2285. Maximum Total Importance of Roads
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.
'''

'''
度最大的加最高的权重,你们怎么知道我的运行时间打败了100%的人
'''

class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        con = [0]*n
        for r in roads:
            for node in r:
                con[node] += 1
        con.sort()
        ans = 0
        for i in range(n-1,-1,-1):
            if con[i] == 0:
                break
            else:
                ans += con[i]*(i+1)
        return ans