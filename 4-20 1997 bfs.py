'''
1971. Find if Path Exists in Graph
Easy
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
'''

'''
第一反应是最小生成树，但easy题能够是最小生成树吗？
'''

'''
看了看答案，bfs的时间复杂度是O(n+m)也许能过
'''


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = [False]*n
        seen[source] = True
        queue = collections.deque([source])
        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            for node in graph[curr]:
                if not seen[node]:
                    seen[node] = True
                    queue.append(node)
        return False
        