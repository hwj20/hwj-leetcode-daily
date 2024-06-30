'''
1579
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
'''

'''
删掉最多的边使得图依然visitable for two persons;;;;为了删这个点把脑袋都想秃了，答案是并查集哈哈哈
'''


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.component_count = size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.component_count -= 1
            return True
        return False

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        
        edges_used = 0
        
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 3:
                ua = uf_alice.union(u, v)
                ub = uf_bob.union(u, v)
                if ua or ub:
                    edges_used += 1
                    # print(t,u,v)
        
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 1:
                if uf_alice.union(u, v):
                    edges_used += 1
            elif t == 2:
                if uf_bob.union(u, v):
                    edges_used += 1
        
        if uf_alice.component_count != 1 or uf_bob.component_count != 1:
            return -1
        
        return len(edges) - edges_used

        # global ans
        # ans = 0
        # count = [0]*3
        # # part = [0]*3
        # m = [defaultdict(list) for _ in range(3)]
        # for e in edges:
        #     count[e[0]-1] += 1
        #     m[e[0]-1][e[1]-1].append(e[2]-1)
        #     m[e[0]-1][e[2]-1].append(e[1]-1)

        # def dfs(now,t,v,fa):
        #     global ans
        #     v[now] = True
        #     for d in m[t][now]:
        #         if not v[d]:
        #             dfs(d,t,v,now)
        #         # 确定不会重复计数
        #         elif fa != d and t != 2 and not (vis[2][d] and vis[2][now]):
        #             print(now,d,t)
        #             ans += 1

        # vis =[[False]*n for _ in range(3)]
        # for i in range(n):
        #     if vis[2][i]:
        #         continue
        #     else:
        #         vis[2] = [False]*n
        #         for j in range(2,-1,-1):
        #             if not vis[j][i] and m[j][i] != []:
        #                 # part[i] += 1
        #                 dfs(i,j,vis[j],-1)
        #         # 删除和type3重复的边
        #         for e in edges:
        #             if e[0] != 3 and vis[2][e[1]-1] and vis[2][e[2]-1]:
        #                 ans += 1

        
        # # 判断连通
        # for i in range(n):
        #     if not vis[2][i]:
        #         if not (vis[0][i] and vis[1][i]):
        #             return -1
        # print(ans)
        # # # 删除和type3重复的边
        # # for e in edges:
        # #     if e[0] != 3 and vis[2][e[1]-1] and vis[2][e[2]-1]:
        # #         ans += 1

        # # for j in range(2):
        # #     ans += count[j]-sum(vis[j])+1+part[j]
        # return ans