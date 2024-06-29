'''
2192
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.
'''

'''
直接dfs? 正解是拓扑排序
'''

class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        e = defaultdict(list)
        ans = [[] for _ in range(n)]
        for edge in edges:
            e[edge[0]].append(edge[1])

        print(e)
        v = [False]*n
        def dfs(now,a):
            # print(now,a)
            v[now] = True
            if a != now:
                ans[now].append(a)
            for d in e[now]:
                if not v[d]:
                    dfs(d,a)

        for i in range(n):
            v = [False]*n
            dfs(i,i)
        ans= [sorted(l) for l in ans]
        return ans        
        
# print(Solution().getAncestors(n=8,edges=[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))