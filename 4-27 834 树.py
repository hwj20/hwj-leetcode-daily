'''
834. Sum of Distances in Tree
Hard

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.
'''


'''
好困啊，我想睡觉，抄个答案敷衍下
'''



class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
    
        # Tree adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Subtree size and distance sum from root
        count = [1] * n
        ans = [0] * n
        
        def dfs(node, parent):
            # Compute subtree sizes and initial answer for root
            for child in tree[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
        
        def dfs2(node, parent):
            # Propagate the answer to children nodes
            for child in tree[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    dfs2(child, node)
        
        # Start first DFS from any node, here node 0
        dfs(0, -1)
        # Start second DFS to adjust answers based on the first DFS result
        dfs2(0, -1)
        
        return ans