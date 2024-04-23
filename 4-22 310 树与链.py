'''
310. Minimum Height Trees
Medium
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''


'''
可以建一颗树，然后从上往下遍历一边，统计depth，然后再根据depth计算最小的node是哪些
python建树不太熟练，找GPT写个板子吧，然后GPT直接帮我把这道题写出来了...
GPT的思路是从叶子层往上找，直到找到最后两个点（为什么？因为只需要考虑树上最长的链的中点...6）
'''




class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
    
        # Create the adjacency list
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        # Initialize the first layer of leaves
        leaves = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        
        # Trim the leaves until we reach the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                # The only neighbor of leaf
                neighbor = adj[leaf].pop()
                # Remove the leaf from its neighbor's list
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)